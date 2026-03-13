# Implementation Plan: Church Sound Assistant

**Branch**: `001-church-sound-assistant` | **Date**: 2026-03-12 | **Spec**: [specs/001-church-sound-assistant/spec.md]
**Input**: Feature specification for a Sound Technician Assistant.

## Summary
Este plano detalha a implementação de um sistema de controle remoto para sonoplastia, composto por um **Host (Python)** que controla o PC Windows e um **Client (React Native)** para controle móvel. A comunicação será via **TCP Sockets** em rede local WiFi, com pareamento simplificado via **QR Code**.

## Technical Context

**Language/Version**: Python 3.10+ (Host), React Native/TypeScript (Client)  
**Primary Dependencies**: `pyautogui`, `yt-dlp`, `qrcode`, `socket` (Host); `react-native-tcp-socket`, `react-native-camera-kit` (Client)  
**Storage**: JSON local para cronogramas e configurações de pasta.  
**Testing**: `pytest` (Host), `Jest` + `React Native Testing Library` (Client)  
**Target Platform**: Windows 10/11 (Host), Android/iOS (Client)
**Project Type**: Desktop Overlay + Mobile App  
**Performance Goals**: Latência de comando < 200ms em rede local.  
**Constraints**: Dependência de rede local WiFi (sem isolamento de AP).  

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- [x] **Clean Code & Modularidade**: O projeto será dividido em módulos claros (SocketServer, MediaController, YTDownloader).
- [x] **Documentação Proativa**: Arquivos `research.md`, `data-model.md`, `contracts/` e `quickstart.md` foram gerados.
- [x] **Testes como Requisito**: O plano de tarefas incluirá fases de testes unitários para o protocolo de socket.
- [x] **Performance e Baixa Latência**: Escolha de TCP Sockets garante a latência mínima.

## Project Structure

### Documentation (this feature)

```text
specs/001-church-sound-assistant/
├── plan.md              # Este arquivo
├── research.md          # Decisões técnicas e ferramentas
├── data-model.md        # Entidades e regras de validação
├── quickstart.md        # Guia de configuração rápida
├── contracts/           # Protocolo de comandos via Socket
└── tasks.md             # Criado pelo comando /speckit.tasks
```

### Source Code (repository root)

```text
server/                  # Host Python
├── main.py              # Ponto de entrada (Overlay UI)
├── core/
│   ├── socket_server.py # Gerenciamento de conexões
│   ├── controller.py    # Integração com PyAutoGUI e VLC
│   └── youtube.py       # Busca e download via yt-dlp
├── tests/
│   └── test_protocol.py # Testes de integridade do socket
└── requirements.txt

mobile/                  # Client React Native
├── src/
│   ├── components/      # UI: Botões de mídia, Chat, Busca
│   ├── services/        # Cliente Socket TCP
│   └── navigation/      # Fluxos: Connect, Control, Schedule
├── tests/
│   └── test_commands.js # Testes de envio de comandos
└── package.json
```

**Structure Decision**: Utilização de uma estrutura híbrida com `server/` (Host) e `mobile/` (Client) para separar claramente as responsabilidades de plataforma.

## Phases

### Phase 0: Setup & Infrastructure
- Inicialização dos repositórios locais para server e mobile.
- Implementação do servidor socket básico no Python.
- Configuração do cliente socket básico no React Native.

### Phase 1: Core Features (P1)
- Implementação do pareamento via QR Code (Host gera, Client escaneia).
- Controle básico de mídia (VLC: Play/Pause/Volume) via socket.

### Phase 2: YouTube & Media (P2)
- Busca de vídeos no Client e abertura remota no Host.
- Implementação de downloads do YouTube em segundo plano no Host.
- Sistema de Cronograma (fila de reprodução).

### Phase 3: Communication & File Transfer (P3)
- Implementação do Chat em tempo real.
- Transferência de arquivos com autenticação de senha global.
- Interface de Overlay no Host para monitoramento.

## Complexity Tracking

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| Múltiplos clientes | Permite equipe colaborativa | Único cliente limitaria a operação do culto |
