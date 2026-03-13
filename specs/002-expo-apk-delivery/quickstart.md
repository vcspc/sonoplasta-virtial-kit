# Quickstart: Gerando APK via Expo (EAS)

Este guia orienta o processo de build do APK para testes em dispositivos físicos Android.

## 1. Pré-requisitos
- Conta ativa em [expo.dev](https://expo.dev).
- Node.js instalado.
- EAS CLI instalado globalmente:
  ```bash
  npm install -g eas-cli
  ```

## 2. Login e Configuração
```bash
# Na pasta mobile
eas login
eas build:configure
```

## 3. Gerando o APK (Preview)
O perfil `preview` está configurado no `eas.json` para gerar um arquivo `.apk` pronto para instalação.
```bash
eas build --profile preview --platform android
```

## 4. Instalação
1. Após o build, o EAS fornecerá uma URL para download ou um **QR Code**.
2. No seu aparelho Android, acesse o link/leia o QR Code.
3. Baixe o arquivo `.apk`.
4. Permita a "Instalação de Fontes Desconhecidas" se solicitado pelo Android.
5. Abra o aplicativo e conecte ao Host via WiFi.

---
**Dica**: Para debugar módulos nativos, use `eas build --profile development --platform android` para gerar um build customizado do Expo Go (Development Client).
