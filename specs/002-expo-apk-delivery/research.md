# Research: Expo Android APK Delivery

## Technical Context

- **Platform**: Expo SDK 49+
- **Build Service**: EAS (Expo Application Services)
- **Native Modules**: `react-native-tcp-socket`, `react-native-camera-kit`
- **Artifact**: Android APK (Release/Development)

## Decisions & Rationale

### 1. Fluxo de Build (EAS Build vs Local)
- **Decision**: EAS Build (Cloud).
- **Rationale**: Simplifica a geração do APK eliminando a necessidade de configurar todo o ambiente Android (SDK, JDK, Gradle) na máquina local do desenvolvedor. Permite builds reprodutíveis na nuvem.
- **Alternatives Considered**: Build local via `npx expo run:android` (exige ambiente Android completo configurado).

### 2. Suporte a Módulos Nativos
- **Decision**: Development Builds via `expo-dev-client`.
- **Rationale**: O projeto utiliza `react-native-tcp-socket` e `react-native-camera-kit`, que possuem código nativo. O "Expo Go" padrão não suporta esses módulos. Criar um "Development Build" permite testar esses módulos dentro do ecossistema Expo.
- **Alternatives Considered**: Expo Prebuild (Bare workflow) - adiciona complexidade de manutenção de pastas `android/` e `ios/`.

### 3. Formato do Artefato
- **Decision**: APK (Android Package).
- **Rationale**: Facilita a instalação direta ("sideloading") em qualquer aparelho Android para testes em campo, sem exigir o envio para a Google Play Store (que exigiria formato .aab).
- **Alternatives Considered**: AAB (Android App Bundle) - apenas para publicação na loja.

## Integration Patterns

- **EAS Config**: Uso do arquivo `eas.json` para definir perfis de build (`development`, `preview`).
- **Prebuild**: Execução de `npx expo prebuild` para injetar as configurações nativas antes do build final.
