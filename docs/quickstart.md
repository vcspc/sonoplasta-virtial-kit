# Quickstart: Desenvolvendo no Sonopalsta Virtual Kit

Este guia orienta a configuração dos dois componentes do sistema: o **Host (PC)** e o **Client (Mobile)**.

## 🖥️ Host (Servidor Python)

O Host é responsável por receber comandos da rede e controlar o Windows (VLC, Slides, Janelas).

### Pré-requisitos
- **Python 3.10+**
- **VLC Media Player** instalado no Windows.

### Configuração
```bash
cd server
python -m venv venv
# No Windows:
venv\Scripts\activate
pip install -r requirements.txt
```

### Execução
```bash
python main.py
```
Um **QR Code** aparecerá no canto superior da tela para o pareamento.

---

## 📱 Client (Aplicativo Mobile)

O Client envia comandos para o Host via WiFi.

### Pré-requisitos
- **Node.js 18+**
- **Android Studio** ou **Xcode** (para emulação/build).

### Configuração
```bash
cd mobile
npm install
```

### Execução
```bash
# Para Android
npm run android
# Para iOS
npm run ios
```

---

## 🏗️ Fluxo de Trabalho (SpecKit)

Cada nova funcionalidade segue o ciclo: Especificação -> Plano -> Tarefas -> Implementação.

## ⚖️ Conformidade (Constitution Check)

- **Clean Code**: SOLID e funções comentadas em PT-BR.
- **Latência**: Comandos devem responder em < 200ms.
- **Segurança**: Transferência de arquivos exige senha global.

---
Precisa de ajuda? Abra uma Issue ou consulte a [Constituição](../.specify/memory/constitution.md).
