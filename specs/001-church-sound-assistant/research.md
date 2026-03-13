# Research: Church Sound Assistant

## Technical Context

- **Host (PC)**: Python 3.10+ (Windows 10/11)
- **Client (Mobile)**: React Native (Android/iOS)
- **Communication**: TCP/IP Sockets via Rede Local WiFi
- **Media Control**: VLC Media Player (via HTTP Interface ou Simulação de Teclado)
- **Automation**: PyAutoGUI (para controle de janelas e slides)

## Decisions & Rationale

### 1. Protocolo de Comunicação
- **Decision**: TCP Sockets (persistente).
- **Rationale**: Baixa latência (<200ms) necessária para comandos de mídia em tempo real. WebSockets seriam uma alternativa, mas exigem um servidor web (como Flask/FastAPI) que adicionaria complexidade desnecessária para comandos simples de rede local.
- **Alternatives Considered**: HTTP REST (alta latência), WebSockets (overhead de servidor).

### 2. Controle do VLC Media Player
- **Decision**: Simulação de teclas via `pyautogui` e interface Web HTTP do VLC.
- **Rationale**: `pyautogui` permite controle global (play/pause mesmo sem foco), enquanto a interface HTTP do VLC permite comandos precisos de volume e tempo.
- **Alternatives Considered**: VLC Telnet (mais complexo de configurar para usuários leigos).

### 3. Busca e Download do YouTube
- **Decision**: `yt-dlp` no Host.
- **Rationale**: É a biblioteca mais estável e atualizada para extração de áudio e vídeo do YouTube. A busca será feita via API do YouTube ou web scraping controlado.
- **Alternatives Considered**: `pytube` (instável com mudanças recentes do YouTube).

### 4. Geração de QR Code
- **Decision**: Biblioteca `qrcode` e `Pillow` no Python.
- **Rationale**: Geração rápida e leve de imagens para exibição no overlay do Host.
- **Alternatives Considered**: APIs externas de QR Code (exige internet, viola premissa de rede local offline).

### 5. Transferência de Arquivos
- **Decision**: Transferência de bytes via socket TCP com chunking (pedaços de 4KB).
- **Rationale**: Simples de implementar no mesmo canal de socket e permite controle de progresso.
- **Alternatives Considered**: Servidor FTP temporário (complexidade de portas e firewall).

## Integration Patterns

- **Command Pattern**: Comandos enviados como JSON via socket: `{"cmd": "VLC_PAUSE", "params": {}}`.
- **Observer Pattern**: Host notifica todos os clientes conectados sobre mudanças de estado (ex: nova mensagem no chat).
