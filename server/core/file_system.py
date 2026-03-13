import os
import logging

# Configuração básica de logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class FileSystemService:
    """
    Serviço para busca e listagem de arquivos locais no Host.
    Implementa o requisito FR-010.
    """
    
    def __init__(self, base_path="media"):
        """
        Inicializa o serviço e define a pasta base de busca.
        """
        self.base_path = base_path
        if not os.path.exists(self.base_path):
            os.makedirs(self.base_path)
        
        # Extensões de mídia suportadas
        self.supported_extensions = ('.mp3', '.mp4', '.wav', '.mkv', '.avi', '.wma', '.aac')

    def list_files(self, sub_dir=""):
        """
        Lista arquivos de mídia na pasta configurada.
        Input: sub_dir (str)
        Output: list de dicts com title, path, type
        """
        search_path = os.path.join(self.base_path, sub_dir)
        logging.info(f"Listando arquivos em: {search_path}")
        
        files = []
        try:
            for root, dirs, filenames in os.walk(search_path):
                for filename in filenames:
                    if filename.lower().endswith(self.supported_extensions):
                        full_path = os.path.join(root, filename)
                        files.append({
                            'title': filename,
                            'path': full_path,
                            'type': 'LOCAL_FILE',
                            'size': os.path.getsize(full_path)
                        })
            return files
        except Exception as e:
            logging.error(f"Erro ao listar arquivos: {e}")
            return []

    def get_absolute_path(self, relative_path):
        """
        Converte um caminho relativo ou parcial em absoluto para abertura segura.
        """
        return os.path.abspath(relative_path)

# Teste simples
if __name__ == "__main__":
    service = FileSystemService()
    media_files = service.list_files()
    for f in media_files:
        print(f"{f['title']} - {f['path']}")
