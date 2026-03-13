# Feature Specification: Expo Android APK Delivery

**Feature Branch**: `002-expo-apk-delivery`  
**Created**: 2026-03-12  
**Status**: Draft  
**Input**: Usuário deseja mudar para Expo (Opção 2) e buildar um APK para testar em aparelho Android físico.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Configuração do Ambiente Expo (Priority: P1)

Como desenvolvedor, quero configurar o projeto mobile para utilizar o ecossistema Expo, garantindo que as dependências nativas (como Sockets TCP) sejam compatíveis com o fluxo de build do Expo.

**Why this priority**: É a base necessária para qualquer processo de build ou teste posterior.

**Independent Test**: Executar o comando de inicialização do Expo e verificar se o projeto carrega sem erros de dependência.

**Acceptance Scenarios**:

1. **Given** a pasta `mobile`, **When** as dependências do Expo são instaladas e o `app.json` configurado, **Then** o comando `npx expo start` deve iniciar o servidor de desenvolvimento.

---

### User Story 2 - Geração de Pacote de Instalação APK (Priority: P1)

Como desenvolvedor, quero gerar um arquivo APK instalável para que eu possa testar o aplicativo em um dispositivo Android real sem depender de um emulador ou cabo USB constante.

**Why this priority**: Permite o teste de campo (na igreja/rede local real) com o hardware final.

**Independent Test**: Gerar o arquivo `.apk` e verificar se o tamanho e a assinatura estão corretos para instalação manual.

**Acceptance Scenarios**:

1. **Given** o ambiente Expo configurado, **When** o comando de build (EAS ou local) é executado, **Then** um arquivo com extensão `.apk` deve ser gerado com sucesso.

---

### User Story 3 - Validação em Dispositivo Físico (Priority: P2)

Como sonoplasta, quero instalar o APK no meu celular Android e conectar ao Host via rede WiFi local para validar os controles de mídia.

**Why this priority**: Valida a utilidade final do produto no ambiente de uso real.

**Independent Test**: Instalar o APK, abrir o app, escanear o QR Code do Host e disparar um comando de "Play".

**Acceptance Scenarios**:

1. **Given** o APK instalado no celular, **When** o usuário abre o aplicativo e realiza o pareamento, **Then** a comunicação via socket deve funcionar exatamente como na versão de desenvolvimento.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: O sistema DEVE utilizar o Expo SDK (versão compatível com as libs atuais) para gerenciar o ciclo de vida do aplicativo.
- **FR-002**: O projeto DEVE possuir um arquivo `app.json` (ou `app.config.js`) configurado com o slug e nome do projeto.
- **FR-003**: O build DEVE incluir os módulos nativos necessários (ex: `react-native-tcp-socket`) através de "Development Builds" ou pré-build.
- **FR-004**: O processo de build DEVE gerar um artefato no formato `.apk` (Android Package).
- **FR-005**: O aplicativo gerado DEVE permitir a instalação via "Sideloading" (fontes desconhecidas) no Android.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: O tempo de build (da execução do comando até o APK pronto) deve ser inferior a 15 minutos (usando EAS remoto ou build local potente).
- **SC-002**: 100% das funcionalidades de conectividade (Socket TCP) validadas na especificação 001 devem permanecer operacionais no APK.
- **SC-003**: O APK deve ser instalável em versões do Android a partir da 10.0.

## Assumptions

- O desenvolvedor possui uma conta no Expo (EAS) ou ambiente local configurado com Android Studio/JDK para build local.
- O dispositivo físico Android e o Host (PC) estão na mesma sub-rede WiFi.
