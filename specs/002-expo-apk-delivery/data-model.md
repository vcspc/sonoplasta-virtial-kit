# App Configuration: Expo Android APK Delivery

## App Configuration (app.json)
- `name`: "Church Sound Assistant"
- `slug`: "church-sound-assistant"
- `version`: "1.0.0"
- `orientation`: "portrait"
- `icon`: "./assets/icon.png"
- `android.package`: "com.sonopalsta.virtualkit"
- `plugins`:
    - `react-native-tcp-socket`
    - `react-native-camera-kit`

## Environment Variables (Build Time)
- `EXPO_PUBLIC_SOCKET_PORT`: Default 5000
- `EXPO_PUBLIC_API_TIMEOUT`: Default 5000ms
