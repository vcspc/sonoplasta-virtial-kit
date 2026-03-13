# Quickstart: Church Sound Assistant

Este guia ajudará você a configurar o ambiente de desenvolvimento para o Host (PC) e o Client (Mobile).

## 🖥️ Host (Python)

### 1. Pré-requisitos
- Python 3.10 ou superior instalado no Windows.
- VLC Media Player instalado (em `C:\Program Files\VideoLAN\VLC\vlc.exe`).

### 2. Instalação
```bash
# Entre na pasta do host
cd server

# Crie um ambiente virtual
python -m venv venv
source venv/Scripts/activate

# Instale as dependências
pip install -r requirements.txt
```

### 3. Execução
```bash
python main.py
```
O Host abrirá uma interface sobreposta exibindo um **QR Code** para conexão.

---

## 📱 Client (React Native)

### 1. Pré-requisitos
- Node.js (v18+)
- React Native CLI
- Android Studio (para emulador Android) ou Xcode (para iOS)

### 2. Instalação
```bash
# Entre na pasta do cliente
cd mobile

# Instale as dependências
npm install
```

### 3. Execução
```bash
# Para Android
npm run android

# Para iOS
npm run ios
```

## 🔗 Pareamento
1. Abra o aplicativo no celular.
2. Clique em **Conectar via QR Code**.
3. Aponte a câmera para o monitor do PC.
4. Após o pareamento, os botões de controle de mídia estarão ativos.
