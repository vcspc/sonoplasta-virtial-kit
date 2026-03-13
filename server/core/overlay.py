import tkinter as tk
from PIL import ImageTk, Image
import logging
import threading

class HostOverlay:
    """
    Interface sobreposta (Overlay) para o Host PC.
    Exibe QR Code, Chat e Logs de comandos.
    Implementa o requisito FR-012.
    """
    
    def __init__(self):
        self.root = None
        self.chat_list = None
        self.log_list = None
        self.qr_label = None
        self.is_running = False

    def setup_ui(self):
        """
        Configura a janela do tkinter para ser um overlay sempre no topo.
        """
        self.root = tk.Tk()
        self.root.title("Sonoplasta Virtual Kit - Overlay")
        
        # Configurações de overlay: sempre no topo, sem bordas, fundo semi-transparente
        self.root.attributes("-topmost", True)
        self.root.geometry("400x600+10+10") # Canto superior esquerdo
        self.root.configure(bg='#1e1e1e')
        
        # Título
        tk.Label(self.root, text="PAINEL DE CONTROLE", fg="yellow", bg="#1e1e1e", font=("Arial", 12, "bold")).pack(pady=5)

        # Área do QR Code
        tk.Label(self.root, text="Conectar Celular:", fg="white", bg="#1e1e1e").pack()
        self.qr_label = tk.Label(self.root, bg="white")
        self.qr_label.pack(pady=5)
        self.update_qr_image()

        # Área de Chat
        tk.Label(self.root, text="Chat em Tempo Real:", fg="white", bg="#1e1e1e").pack()
        self.chat_list = tk.Listbox(self.root, bg="#2d2d2d", fg="lightgreen", height=8, width=50, borderwidth=0)
        self.chat_list.pack(padx=10, pady=5)

        # Área de Logs
        tk.Label(self.root, text="Log de Comandos:", fg="white", bg="#1e1e1e").pack()
        self.log_list = tk.Listbox(self.root, bg="#2d2d2d", fg="white", height=8, width=50, borderwidth=0)
        self.log_list.pack(padx=10, pady=5)

        self.add_log("Sistema pronto e aguardando...")

    def update_qr_image(self, path="connection_qr.png"):
        """
        Atualiza a imagem do QR Code no painel.
        """
        try:
            img = Image.open(path)
            img = img.resize((150, 150), Image.LANCZOS)
            photo = ImageTk.PhotoImage(img)
            self.qr_label.config(image=photo)
            self.qr_label.image = photo
        except Exception as e:
            logging.error(f"Erro ao carregar QR Code no overlay: {e}")

    def add_chat_msg(self, sender, message):
        """
        Adiciona uma mensagem de chat à lista.
        """
        if self.chat_list:
            self.chat_list.insert(tk.END, f"{sender}: {message}")
            self.chat_list.see(tk.END) # Scroll automático

    def add_log(self, message):
        """
        Adiciona um log de sistema à lista.
        """
        if self.log_list:
            self.log_list.insert(tk.END, f"> {message}")
            self.log_list.see(tk.END)

    def start(self):
        """
        Inicia o loop principal da interface.
        """
        self.is_running = True
        self.setup_ui()
        self.root.mainloop()

    def stop(self):
        """
        Encerra a interface.
        """
        if self.root:
            self.root.quit()
            self.is_running = False

# Exemplo de teste isolado
if __name__ == "__main__":
    overlay = HostOverlay()
    overlay.start()
