import json
import logging

# Configuração básica de logging em português conforme a constituição
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class CommandValidator:
    """
    Validador de protocolos para comandos JSON recebidos via Socket.
    Garante a conformidade com contracts/socket-protocol.md.
    """
    
    REQUIRED_FIELDS = ['type', 'payload']
    
    VALID_COMMAND_TYPES = [
        'VLC_CMD', 
        'YT_SEARCH', 
        'YT_DOWNLOAD', 
        'SLIDE_CMD', 
        'FILE_SEARCH', 
        'FILE_XFER_START', 
        'CHAT_MSG'
    ]

    @staticmethod
    def validate(command_dict):
        """
        Valida se o dicionário de comando segue o contrato.
        Input: command_dict (dict)
        Output: (bool, str) - Sucesso e mensagem de erro se houver.
        """
        # Verifica campos obrigatórios
        for field in CommandValidator.REQUIRED_FIELDS:
            if field not in command_dict:
                return False, f"Campo obrigatório ausente: {field}"
        
        # Verifica tipo de comando
        cmd_type = command_dict.get('type')
        if cmd_type not in CommandValidator.VALID_COMMAND_TYPES:
            return False, f"Tipo de comando inválido: {cmd_type}"
            
        # Validações específicas por tipo de comando
        payload = command_dict.get('payload')
        
        if cmd_type == 'VLC_CMD':
            if 'action' not in payload:
                return False, "Payload de VLC_CMD deve conter 'action'"
                
        if cmd_type == 'YT_SEARCH':
            if 'query' not in payload:
                return False, "Payload de YT_SEARCH deve conter 'query'"
                
        if cmd_type == 'FILE_XFER_START':
            if not all(k in payload for k in ('filename', 'size', 'password')):
                return False, "Payload de FILE_XFER_START incompleto"
        
        return True, "Válido"

    @staticmethod
    def parse_and_validate(json_string):
        """
        Converte string para JSON e valida.
        Input: json_string (str)
        Output: (dict, str) - Dicionário parseado ou None e mensagem de erro.
        """
        try:
            data = json.loads(json_string)
            is_valid, error_msg = CommandValidator.validate(data)
            if is_valid:
                return data, "Válido"
            else:
                return None, error_msg
        except json.JSONDecodeError:
            return None, "Erro de decodificação JSON"
        except Exception as e:
            return None, f"Erro inesperado no parser: {e}"

# Exemplo de uso
if __name__ == "__main__":
    test_cmd = {"type": "VLC_CMD", "payload": {"action": "PLAY"}}
    valid, msg = CommandValidator.validate(test_cmd)
    logging.info(f"Teste de validação: {valid} - {msg}")
