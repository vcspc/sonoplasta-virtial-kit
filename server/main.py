import sys
import logging
import json
import threading
from core.socket_server import SocketServer
from core.discovery import Discovery
from core.controller import MediaController
from core.protocol import CommandValidator
from core.youtube import YouTubeService
from core.file_system import FileSystemService
from core.schedule import ScheduleManager
from core.logger import setup_logger, handle_exception
from core.overlay import HostOverlay
from core.notifications import NotificationService

class HostApplication:
    """
    Aplicação principal do Host PC para o Sonoplasta Virtual Kit.
    Orquestra o servidor socket, interface overlay e serviços do sistema.
    """
    
    def __init__(self):
        # Configura logging e exceções
        self.logger = setup_logger()
        sys.excepthook = handle_exception
        
        # Componentes Core
        self.discovery = Discovery()
        self.media_controller = MediaController()
        self.youtube_service = YouTubeService()
        self.file_service = FileSystemService()
        self.schedule_manager = ScheduleManager()
        self.notifier = NotificationService()
        
        # Interface e Servidor
        self.overlay = HostOverlay()
        self.server = SocketServer()
        
        logging.info("Aplicação Host inicializada com Overlay.")

    def run(self):
        """
        Inicia o servidor em background e o overlay no foreground.
        """
        # 1. Gera QR Code inicial
        Discovery.generate_connection_qr(port=5000)
        
        # 2. Inicia servidor Socket em uma thread separada
        server_thread = threading.Thread(target=self.start_socket_server)
        server_thread.daemon = True
        server_thread.start()
        
        # 3. Inicia Interface Overlay (Bloqueia a thread principal)
        logging.info("Iniciando interface overlay...")
        self.overlay.start()

    def start_socket_server(self):
        """
        Método auxiliar para rodar o servidor em thread.
        """
        self.server.start(self.process_command)

    def process_command(self, command, client_socket):
        """
        Callback de processamento de comandos recebidos via rede.
        """
        is_valid, msg = CommandValidator.validate(command)
        if not is_valid:
            return

        cmd_type = command.get('type')
        payload = command.get('payload', {})

        # Loga no overlay
        self.overlay.add_log(f"Comando: {cmd_type}")

        # Roteamento
        if cmd_type == 'VLC_CMD':
            self.media_controller.execute_vlc_command(payload.get('action'))
        
        elif cmd_type == 'SLIDE_CMD':
            self.media_controller.control_slides(payload.get('action'))

        elif cmd_type == 'YT_SEARCH':
            results = self.youtube_service.search(payload.get('query'))
            self.server.broadcast({"type": "YT_SEARCH_RESULTS", "payload": {"results": results}})

        elif cmd_type == 'YT_DOWNLOAD':
            self.youtube_service.download(payload.get('url'), mode=payload.get('mode'))

        elif cmd_type == 'YT_OPEN':
            self.media_controller.open_youtube(payload.get('url'))

        elif cmd_type == 'CHAT_MSG':
            sender = payload.get('sender', 'Cliente')
            message = payload.get('content', '')
            # Atualiza UI do Overlay
            self.overlay.add_chat_msg(sender, message)
            # Notifica o sistema
            self.notifier.notify(f"Chat de {sender}", message)
            # Broadcast para outros clientes
            self.server.broadcast(command)
            
        # ... outros comandos (FILE_SEARCH, SCHEDULE, etc) ...

        # ACK
        try:
            ack = {"type": "ACK", "payload": {"id": command.get('id'), "status": "success"}}
            client_socket.sendall((json.dumps(ack) + "\n").encode('utf-8'))
        except:
            pass

    def stop(self):
        self.server.stop()
        self.overlay.stop()
        logging.info("Aplicação Host encerrada.")

if __name__ == "__main__":
    app = HostApplication()
    try:
        app.run()
    except KeyboardInterrupt:
        app.stop()
