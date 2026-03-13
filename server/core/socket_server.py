import socket
import threading
import json
import logging
import os

# Configuração básica de logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SocketServer:
    """
    Servidor TCP multithreaded para gerenciar conexões e transferência de arquivos.
    Implementa o requisito FR-009 e FR-014.
    """
    
    def __init__(self, host='0.0.0.0', port=5000, password="admin_sonoplasta"):
        self.host = host
        self.port = port
        self.global_password = password
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.clients = []
        self.is_running = False

    def start(self, callback):
        try:
            self.server_socket.bind((self.host, self.port))
            self.server_socket.listen(5)
            self.is_running = True
            logging.info(f"Servidor iniciado em {self.host}:{self.port}")
            
            while self.is_running:
                client_socket, address = self.server_socket.accept()
                logging.info(f"Nova conexão de {address}")
                self.clients.append(client_socket)
                
                client_thread = threading.Thread(
                    target=self.handle_client, 
                    args=(client_socket, address, callback)
                )
                client_thread.daemon = True
                client_thread.start()
                
        except Exception as e:
            logging.error(f"Erro ao iniciar servidor: {e}")
        finally:
            self.stop()

    def handle_client(self, client_socket, address, callback):
        buffer = ""
        try:
            while self.is_running:
                data = client_socket.recv(4096)
                if not data:
                    break
                
                try:
                    text_data = data.decode('utf-8')
                    buffer += text_data
                    
                    while "\n" in buffer:
                        line, buffer = buffer.split("\n", 1)
                        if line.strip():
                            command = json.loads(line)
                            
                            # Lógica Especial: Início de Transferência de Arquivo
                            if command.get('type') == 'FILE_XFER_START':
                                self.handle_file_transfer(client_socket, command.get('payload'))
                            else:
                                callback(command, client_socket)
                except UnicodeDecodeError:
                    # Se falhar o decode, ignoramos ou tratamos como erro de protocolo
                    # (Binários são tratados dentro de handle_file_transfer)
                    pass

        except Exception as e:
            logging.error(f"Erro na conexão com {address}: {e}")
        finally:
            if client_socket in self.clients:
                self.clients.remove(client_socket)
            client_socket.close()

    def handle_file_transfer(self, client_socket, payload):
        """
        Gerencia o recebimento de bytes de um arquivo.
        """
        filename = payload.get('filename')
        filesize = payload.get('size')
        password = payload.get('password')

        if password != self.global_password:
            logging.warning(f"Tentativa de transferência com senha errada: {filename}")
            client_socket.sendall(b'{"type": "ERROR", "payload": "Senha incorreta"}\n')
            return

        logging.info(f"Recebendo arquivo: {filename} ({filesize} bytes)")
        save_path = os.path.join("media", filename)
        
        try:
            client_socket.sendall(b'{"type": "READY_FOR_DATA"}\n')
            
            with open(save_path, 'wb') as f:
                bytes_received = 0
                while bytes_received < filesize:
                    chunk = client_socket.recv(min(4096, filesize - bytes_received))
                    if not chunk:
                        break
                    f.write(chunk)
                    bytes_received += len(chunk)
            
            logging.info(f"Arquivo {filename} recebido com sucesso.")
            client_socket.sendall(b'{"type": "XFER_COMPLETE"}\n')
        except Exception as e:
            logging.error(f"Erro no recebimento do arquivo: {e}")

    def broadcast(self, message):
        msg_str = json.dumps(message) + "\n"
        for client in self.clients:
            try:
                client.sendall(msg_str.encode('utf-8'))
            except:
                pass

    def stop(self):
        self.is_running = False
        for client in self.clients:
            client.close()
        self.server_socket.close()
