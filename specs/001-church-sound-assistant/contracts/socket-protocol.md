# Socket Contract: Church Sound Assistant

## Protocol Overview
- **Type**: TCP Sockets
- **Encoding**: UTF-8
- **Format**: JSON-encoded strings terminated by `\n` (newline)

## Commands (Client → Host)

### VLC Control
```json
{
  "type": "VLC_CMD",
  "payload": {
    "action": "PLAY" | "PAUSE" | "STOP" | "VOL_UP" | "VOL_DOWN" | "FULLSCREEN"
  }
}
```

### YouTube Search
```json
{
  "type": "YT_SEARCH",
  "payload": {
    "query": "musica gospel"
  }
}
```

### YouTube Download
```json
{
  "type": "YT_DOWNLOAD",
  "payload": {
    "url": "https://youtube.com/...",
    "mode": "AUDIO_ONLY" | "VIDEO_AND_AUDIO"
  }
}
```

### File Transfer
```json
{
  "type": "FILE_XFER_START",
  "payload": {
    "filename": "backup.mp4",
    "size": 104857600,
    "password": "hashed_password"
  }
}
```

## Events (Host → Client)

### Notification / Status
```json
{
  "type": "NOTIFY",
  "payload": {
    "message": "Novo arquivo recebido",
    "level": "INFO" | "ERROR"
  }
}
```

### Chat Sync
```json
{
  "type": "CHAT_MSG",
  "payload": {
    "sender": "Operador PC",
    "content": "Aumentando o volume..."
  }
}
```
