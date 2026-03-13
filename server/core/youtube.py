import yt_dlp
import logging
import os
import threading

# Configuração básica de logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class YouTubeService:
    """
    Serviço para busca e download de vídeos do YouTube usando yt-dlp.
    Implementa os requisitos FR-006 e FR-008.
    """
    
    def __init__(self, download_path="downloads"):
        """
        Inicializa o serviço e garante a existência da pasta de downloads.
        """
        self.download_path = download_path
        if not os.path.exists(self.download_path):
            os.makedirs(self.download_path)
        
        # Opções base para busca
        self.search_opts = {
            'format': 'bestaudio/best',
            'noplaylist': True,
            'quiet': True,
            'extract_flat': True,
        }

    def search(self, query, max_results=5):
        """
        Realiza uma busca no YouTube e retorna metadados simplificados.
        Input: query (str), max_results (int)
        Output: list de dicts com title, url, duration, thumbnail
        """
        logging.info(f"Buscando no YouTube: {query}")
        try:
            with yt_dlp.YoutubeDL(self.search_opts) as ydl:
                # Usa o prefixo ytsearch para buscar por termos
                result = ydl.extract_info(f"ytsearch{max_results}:{query}", download=False)
                
                videos = []
                for entry in result.get('entries', []):
                    videos.append({
                        'title': entry.get('title'),
                        'url': entry.get('url') or f"https://www.youtube.com/watch?v={entry.get('id')}",
                        'duration': entry.get('duration'),
                        'id': entry.get('id')
                    })
                return videos
        except Exception as e:
            logging.error(f"Erro na busca do YouTube: {e}")
            return []

    def download(self, url, mode="VIDEO_AND_AUDIO", callback=None):
        """
        Inicia o download de um vídeo em uma thread separada.
        Input: url (str), mode (str), callback (func opcional)
        """
        def run_download():
            opts = {
                'outtmpl': os.path.join(self.download_path, '%(title)s.%(ext)s'),
                'quiet': True,
            }
            
            if mode == "AUDIO_ONLY":
                opts.update({
                    'format': 'bestaudio/best',
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': '192',
                    }],
                })
            
            try:
                logging.info(f"Iniciando download ({mode}): {url}")
                with yt_dlp.YoutubeDL(opts) as ydl:
                    ydl.download([url])
                logging.info(f"Download concluído: {url}")
                if callback:
                    callback(True, url)
            except Exception as e:
                logging.error(f"Erro no download: {e}")
                if callback:
                    callback(False, url)

        thread = threading.Thread(target=run_download)
        thread.daemon = True
        thread.start()

# Teste simples
if __name__ == "__main__":
    service = YouTubeService()
    results = service.search("hino vitoria")
    for r in results:
        print(f"{r['title']} - {r['url']}")
