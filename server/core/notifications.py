import logging
import platform
import os

# Configuração básica de logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class NotificationService:
    """
    Sistema de notificações para o operador do Host.
    Implementa o requisito de notificação visual.
    """
    
    def __init__(self):
        self.system = platform.system()
        logging.info(f"Serviço de notificação inicializado para {self.system}")

    def notify(self, title, message):
        """
        Exibe uma notificação no sistema operacional.
        Input: title (str), message (str)
        """
        logging.info(f"Notificação: {title} - {message}")
        
        try:
            if self.system == "Windows":
                # Tenta usar win10toast se disponível, senão fallback para comando powershell
                try:
                    from win10toast import ToastNotifier
                    toaster = ToastNotifier()
                    toaster.show_toast(title, message, duration=5, threaded=True)
                except ImportError:
                    # Fallback usando PowerShell para evitar dependência externa obrigatória agora
                    command = f'powershell.exe -Command "Add-Type -AssemblyName System.Windows.Forms; [System.Windows.Forms.MessageBox]::Show(\'{message}\', \'{title}\')"'
                    # Nota: MessageBox é bloqueante, ideal seria BalloonTip. 
                    # Para não bloquear a thread do socket, usaremos apenas log por enquanto 
                    # se win10toast não estiver presente, ou um comando não-bloqueante.
                    logging.info("Win10toast não encontrado. Notificação enviada ao log.")
            
            elif self.system == "Linux":
                os.system(f'notify-send "{title}" "{message}"')
                
        except Exception as e:
            logging.error(f"Erro ao exibir notificação: {e}")

# Exemplo de uso
if __name__ == "__main__":
    notifier = NotificationService()
    notifier.notify("Teste", "Mensagem de teste do sistema")
