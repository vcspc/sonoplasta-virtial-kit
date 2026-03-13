# Implementation Plan: Expo Android APK Delivery

**Branch**: `002-expo-apk-delivery` | **Date**: 2026-03-12 | **Spec**: [specs/002-expo-apk-delivery/spec.md]
**Input**: Usuário deseja mudar para Expo e buildar um APK para Android físico.

## Summary
Este plano detalha a migração do fluxo de desenvolvimento mobile para o **Expo SDK**, utilizando o **EAS Build** para gerar artefatos APK. A estratégia foca no suporte a módulos nativos (Socket TCP) através de **Development Builds**, permitindo testes reais em dispositivos Android físicos.

## Technical Context

**Language/Version**: TypeScript / Expo SDK 49+
**Primary Dependencies**: `expo`, `expo-dev-client`, `eas-cli`, `react-native-tcp-socket`
**Target Platform**: Android (API 29+)
**Build System**: EAS Build (Cloud)
**Artifact Format**: APK (Release/Preview)

## Constitution Check

- [x] **Clean Code & Modularidade**: As configurações de build serão isoladas em `app.json` e `eas.json`.
- [x] **Documentação Proativa**: Guia de build e configuração (`quickstart.md`, `research.md`) gerados.
- [x] **Testes como Requisito**: O plano inclui validação de conectividade pós-build no APK.
- [x] **Performance**: O uso de APK nativo gerado pelo Expo mantém a baixa latência dos Sockets.

## Project Structure

### Documentation (this feature)

```text
specs/002-expo-apk-delivery/
├── plan.md              # Este arquivo
├── research.md          # Decisões sobre EAS e Native Modules
├── data-model.md        # Configurações do app.json
├── quickstart.md        # Guia de execução do build EAS
├── contracts/           # Definição do eas.json
└── tasks.md             # Criado pelo comando /speckit.tasks
```

### Source Code Updates (mobile/)

```text
mobile/
├── app.json             # Configuração global do Expo
├── eas.json             # Perfis de build (APK)
├── babel.config.js      # Ajustes para Expo
└── package.json         # Scripts do Expo
```

## Phases

### Phase 0: Expo Initialization
- Instalação do core do Expo e dependências do SDK.
- Configuração do ponto de entrada (`AppEntry.js`).
- Ajuste do `package.json` com scripts `expo start`, `expo run:android`.

### Phase 1: EAS Configuration
- Instalação do `eas-cli`.
- Criação do `eas.json` com perfil de build `preview` (tipo APK).
- Configuração do `app.json` com plugins nativos (`tcp-socket`).

### Phase 2: Build & Artifact Generation
- Execução do login e configuração no EAS.
- Disparo do build remoto para Android.
- Download e armazenamento do APK gerado.

### Phase 3: Hardware Validation
- Instalação do APK no aparelho físico.
- Teste de pareamento via QR Code e comandos de mídia.
- Validação final de latência e estabilidade da rede.

## Complexity Tracking

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| Development Builds | Suporte a Sockets TCP nativos | Expo Go padrão não suporta sockets TCP |
