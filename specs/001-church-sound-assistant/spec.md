# Feature Specification: Church Sound Assistant

**Feature Branch**: `001-church-sound-assistant`  
**Created**: 2026-03-12  
**Status**: Draft  
**Input**: User description of a church sound technician assistant (Host: Python/PC, Client: React Native/Mobile).

## Clarifications

### Session 2026-03-12
- Q: O download do YouTube deve suportar apenas áudio ou vídeo também? → A: Deve ser áudio e vídeo.
- Q: A senha para transferência é por sessão ou global? → A: Deve ser uma senha global definida no host.
- Q: Qual o protocolo de comunicação preferencial para o envio de comandos entre o celular e o PC? → A: TCP/IP Sockets (Baixa latência, conexão persistente).
- Q: Qual o limite de tamanho para a transferência de arquivos entre o celular e o PC? → A: 500 MB (Ideal para mídias de apresentação).
- Q: O sistema deve permitir múltiplos clientes conectados simultaneamente ao mesmo Host? → A: Múltiplos clientes simultâneos.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Conexão e Controle Remoto de Mídia (Priority: P1)

Como sonoplasta, quero conectar meu celular ao computador via QR Code para controlar a reprodução de áudio e vídeo (VLC) sem precisar estar fisicamente no computador.

**Why this priority**: É a funcionalidade principal que viabiliza o controle remoto básico necessário para o culto.

**Independent Test**: O usuário escaneia o QR Code, a conexão é estabelecida e os comandos de play/pause/volume refletem instantaneamente no VLC do Host.

**Acceptance Scenarios**:

1. **Given** o Host exibindo um QR Code, **When** o Client escaneia o código, **Then** o IP do host é capturado e a conexão via rede local WiFi é estabelecida.
2. **Given** o Client conectado, **When** o usuário clica em "Play" ou "Pause", **Then** o player VLC no computador executa a ação correspondente.
3. **Given** um vídeo ou áudio aberto, **When** o usuário clica em "Tela Cheia", **Then** o VLC entra no modo de tela cheia no monitor principal do Host.

---

### User Story 2 - Projeção de Vídeos do YouTube (Priority: P2)

Como sonoplasta, quero buscar vídeos do YouTube no celular e abri-los diretamente no navegador do computador em tela cheia para facilitar a exibição de conteúdos espontâneos.

**Why this priority**: Agiliza a busca de conteúdo externo durante o evento.

**Independent Test**: Realizar uma busca no Client, clicar em um vídeo e verificar se ele abre no navegador padrão do Host já em modo "full screen".

**Acceptance Scenarios**:

1. **Given** a ferramenta de busca de vídeo no Client, **When** o usuário digita um termo e clica em um resultado, **Then** o Host abre o navegador padrão na URL do vídeo.
2. **Given** o vídeo abrindo no Host, **When** a página carrega, **Then** o sistema deve forçar o modo de tela cheia automaticamente.

---

### User Story 3 - Organização e Cronograma (Priority: P2)

Como sonoplasta, quero organizar uma fila de reprodução (links e arquivos locais) para seguir o roteiro do culto de forma ordenada.

**Why this priority**: Garante que o fluxo do evento seja seguido sem interrupções para busca manual de arquivos.

**Independent Test**: Adicionar 3 itens (link YouTube, arquivo local) ao cronograma e disparar a execução sequencial de cada um.

**Acceptance Scenarios**:

1. **Given** a tela de cronograma, **When** o usuário adiciona um arquivo local ou link, **Then** o item aparece na lista organizada.
2. **Given** o cronograma montado, **When** o usuário clica no primeiro item, **Then** o Host executa o recurso correspondente.

---

### User Story 4 - Comunicação e Monitoramento (Priority: P3)

Como sonoplasta no computador, quero receber notificações de mensagens do celular para coordenar ações com quem está no controle móvel.

**Why this priority**: Melhora a coordenação entre a equipe técnica.

**Acceptance Scenarios**:

1. **Given** o chat aberto no Client, **When** o usuário envia uma mensagem, **Then** o Host exibe uma notificação visual e adiciona a mensagem à interface sobreposta.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: O Host DEVE gerar um QR Code contendo o endereço IP local e porta de conexão.
- **FR-002**: O Client DEVE escanear o QR Code e persistir o IP para conexões futuras na mesma sessão.
- **FR-003**: O sistema DEVE enviar comandos de Play, Pause, Volume +/- e Fullscreen para o VLC Media Player via rede WiFi utilizando TCP/IP Sockets.
- **FR-004**: O Host DEVE possibilitar o fechamento de janelas ativas por comando remoto.
- **FR-005**: O sistema DEVE incluir botões específicos para controle de slides (Próximo/Anterior).
- **FR-006**: O Client DEVE possuir uma ferramenta de busca de vídeos do YouTube via API ou similar.
- **FR-007**: O Host DEVE abrir links do YouTube no navegador padrão e tentar maximizar o vídeo.
- **FR-008**: O sistema DEVE permitir o download de vídeos do YouTube (áudio e vídeo) diretamente pelo Host através de comando do Client.
- **FR-009**: O sistema DEVE permitir a transferência de arquivos de até 500 MB entre Client e Host com autenticação por uma senha global definida no Host.
- **FR-010**: O Client DEVE buscar arquivos em uma pasta pré-configurada no Host e disparar sua abertura remota.
- **FR-011**: O sistema DEVE implementar um Chat bidirecional em tempo real entre múltiplos clientes e o Host.
- **FR-012**: O Host DEVE exibir uma interface sobreposta (overlay) com Chat, QR Code e Log de Comandos.
- **FR-013**: O sistema DEVE gerenciar um cronograma de itens (arquivos/links) com suporte a reordenação.
- **FR-014**: O Host DEVE suportar conexões simultâneas de múltiplos Clients, gerenciando o estado de cada sessão de forma independente.

### Key Entities

- **Connection**: Representa a sessão ativa entre o Client (Mobile) e o Host (PC) via socket persistente (suporta múltiplas conexões).
- **Command**: Instrução enviada (ex: VLC_PLAY, VOL_UP, OPEN_FILE).
- **MediaItem**: Representa um vídeo do YouTube ou um arquivo local na pasta de projeto.
- **Schedule**: Coleção ordenada de MediaItems para execução durante o evento.
- **ChatMessage**: Texto enviado entre Client e Host.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: O tempo de resposta entre o clique no celular e a execução no PC deve ser inferior a 200ms em uma rede estável.
- **SC-002**: 100% dos comandos básicos de mídia (Play/Pause) devem ser executados com sucesso se o VLC estiver aberto.
- **SC-003**: A conexão via QR Code deve ser completada em menos de 5 segundos após o scan.
- **SC-004**: A ferramenta de busca de arquivos deve retornar resultados em menos de 1 segundo para pastas com até 500 itens.

## Assumptions

- O Host está rodando em sistema operacional Windows (devido à natureza do controle de janelas e VLC em ambientes de igreja).
- O VLC Media Player está instalado e configurado com a interface web ou de controle remoto ativa (ou o host simulará entradas de teclado).
- A rede local WiFi permite tráfego entre dispositivos (sem isolamento de AP).
- A comunicação via Sockets é permitida pelo Firewall do Host na porta configurada.
