import pyautogui
import logging
import time

# Configuração básica de logging em português conforme a constituição
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class MediaController:
    """
    Controlador de mídia para o VLC Media Player via comandos de teclado.
    Implementa o requisito FR-003.
    """
    
    def __init__(self):
        """
        Inicializa o controlador de mídia.
        """
        # Define um pequeno delay entre comandos para evitar sobrecarga
        pyautogui.PAUSE = 0.1
        logging.info("Controlador de mídia inicializado.")

    def execute_vlc_command(self, action):
        """
        Executa um comando de teclado mapeado para o VLC.
        Input: action (str) - PLAY, PAUSE, VOL_UP, VOL_DOWN, FULLSCREEN
        """
        logging.info(f"Executando comando VLC: {action}")
        
        try:
            if action in ["PLAY", "PAUSE", "TOGGLE"]:
                # VLC usa espaço para alternar play/pause
                pyautogui.press('space')
            
            elif action == "VOL_UP":
                # VLC usa Ctrl + Seta Cima ou apenas Seta Cima dependendo da versão
                pyautogui.press('up')
            
            elif action == "VOL_DOWN":
                pyautogui.press('down')
            
            elif action == "FULLSCREEN":
                # 'f' é o atalho padrão de tela cheia no VLC
                pyautogui.press('f')
            
            elif action == "STOP":
                # 's' para parar a reprodução
                pyautogui.press('s')
                
            else:
                logging.warning(f"Ação VLC desconhecida: {action}")
                return False
                
            return True
            
        except Exception as e:
            logging.error(f"Erro ao executar comando de mídia: {e}")
            return False

    def control_slides(self, direction):
        """
        Controla slides (PowerPoint, PDF, etc) via setas do teclado.
        Input: direction (str) - NEXT, PREV
        """
        logging.info(f"Controlando slides: {direction}")
        try:
            if direction == "NEXT":
                pyautogui.press('right')
            elif direction == "PREV":
                pyautogui.press('left')
            return True
        except Exception as e:
            logging.error(f"Erro ao controlar slides: {e}")
            return False

    def close_window(self):
        """
        Fecha a janela ativa (Alt+F4).
        Implementa o requisito FR-004.
        """
        logging.info("Fechando janela ativa.")
        try:
            pyautogui.hotkey('alt', 'f4')
            return True
        except Exception as e:
            logging.error(f"Erro ao fechar janela: {e}")
            return False

    def open_local_file(self, file_path):
        """
        Abre um arquivo local no Host usando o aplicativo padrão do sistema.
        Implementa o requisito FR-010.
        Input: file_path (str)
        """
        logging.info(f"Abrindo arquivo local: {file_path}")
        try:
            if not os.path.exists(file_path):
                logging.error(f"Arquivo não encontrado: {file_path}")
                return False
                
            # Comando para abrir arquivo no Windows (aplicativo padrão)
            os.startfile(file_path)
            return True
        except Exception as e:
            logging.error(f"Erro ao abrir arquivo local: {e}")
            return False

    def open_youtube(self, url):
        """
        Abre uma URL do YouTube no navegador padrão e tenta colocar em tela cheia.
        Implementa o requisito FR-007.
        Input: url (str)
        """
        import webbrowser
        logging.info(f"Abrindo YouTube: {url}")
        try:
            # Abre a URL no navegador padrão do sistema
            webbrowser.open(url)
            
            # Aguarda um pouco para o navegador abrir e focar
            time.sleep(3)
            
            # Tenta colocar em tela cheia (tecla 'f' no player do YouTube)
            pyautogui.press('f')
            return True
        except Exception as e:
            logging.error(f"Erro ao abrir YouTube no Host: {e}")
            return False

# Exemplo simples de uso
if __name__ == "__main__":
    controller = MediaController()
    time.sleep(2)  # Tempo para o usuário mudar o foco para o VLC
    controller.execute_vlc_command("PLAY")
