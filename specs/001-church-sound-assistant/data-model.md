# Data Model: Church Sound Assistant

## Entities

### Connection
- `id`: string (uuid da sessão)
- `client_ip`: string
- `status`: enum (connected, disconnected, authenticated)
- `last_activity`: datetime

### Command
- `id`: string (uuid)
- `type`: enum (VLC_CMD, YT_SEARCH, YT_DOWNLOAD, SLIDE_CMD, FILE_SEARCH, FILE_XFER, CHAT_MSG)
- `payload`: object (específico por comando)
- `timestamp`: long

### MediaItem
- `id`: string (hash ou uuid)
- `title`: string
- `type`: enum (LOCAL_FILE, YT_LINK)
- `path_or_url`: string
- `metadata`: object (thumbnail, duration)

### Schedule
- `id`: string
- `items`: array (MediaItem ids ordenados)
- `current_index`: integer

### ChatMessage
- `sender`: enum (HOST, CLIENT_ID)
- `content`: string
- `timestamp`: long

## Validation Rules
- **Passwords**: A senha global deve ter no mínimo 6 caracteres para transferências de arquivos.
- **File Transfer**: Tamanho máximo de arquivo: 500MB (validado no envio de metadados).
- **Socket Messages**: Toda mensagem deve ser um JSON válido e conter o campo `type`.
