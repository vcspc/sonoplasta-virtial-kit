import logging
import os
from datetime import datetime

# Cria a pasta de logs se não existir
LOG_DIR = "logs"
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

def setup_logger():
    """
    Configura o sistema de logging centralizado para o Host.
    Registra eventos em arquivo e no console em português.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_file = os.path.join(LOG_DIR, f"host_{timestamp}.log")
    
    # Formato das mensagens
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - [%(module)s] - %(message)s')
    
    # Handler para console
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    
    # Handler para arquivo
    file_handler = logging.FileHandler(log_file, encoding='utf-8')
    file_handler.setFormatter(formatter)
    
    # Configuração do Logger Root
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    
    logging.info("Sistema de logging inicializado com sucesso.")
    return logger

def handle_exception(exc_type, exc_value, exc_traceback):
    """
    Tratamento global de exceções não capturadas.
    """
    if issubclass(exc_type, KeyboardInterrupt):
        logging.info("Aplicação encerrada pelo usuário.")
        return
        
    logging.critical("Exceção não capturada:", exc_info=(exc_type, exc_value, exc_traceback))

# Exemplo de uso para inicializar o sistema de log centralizado
if __name__ == "__main__":
    setup_logger()
    logging.info("Teste de log do sistema.")
    logging.error("Exemplo de erro logado.")
