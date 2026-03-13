import socket
import qrcode
import os
import logging

# Configuração básica de logging em português conforme a constituição
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Discovery:
    """
    Gerencia a descoberta de rede e geração de QR Code para pareamento.
    Implementa o requisito FR-001.
    """
    
    @staticmethod
    def get_local_ip():
        """
        Obtém o endereço IP local da máquina na rede WiFi/Ethernet.
        Output: ip (str)
        """
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            # Não precisa conectar de verdade, apenas para disparar a escolha da interface
            s.connect(('8.8.8.8', 1))
            ip = s.getsockname()[0]
        except Exception:
            ip = '127.0.0.1'
        finally:
            s.close()
        return ip

    @staticmethod
    def generate_connection_qr(port=5000, output_path="connection_qr.png"):
        """
        Gera um QR Code com as informações de conexão do Host.
        Input: port (int), output_path (str)
        Output: dict com info de conexão
        """
        ip = Discovery.get_local_ip()
        connection_info = {
            "ip": ip,
            "port": port,
            "name": "Sonoplasta Virtual Kit Host"
        }
        
        # Converte para string JSON para o QR Code
        import json
        data = json.dumps(connection_info)
        
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        img.save(output_path)
        
        logging.info(f"QR Code de conexão gerado para {ip}:{port} em {output_path}")
        return connection_info

if __name__ == "__main__":
    info = Discovery.generate_connection_qr()
    print(f"Informações de Conexão: {info}")
