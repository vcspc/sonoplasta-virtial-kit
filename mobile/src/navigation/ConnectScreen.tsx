import React, { useState } from 'react';
import { View, Text, StyleSheet, Button, Alert } from 'react-native';
import { CameraScreen } from 'react-native-camera-kit';
import SocketClient from '../services/socket_client';

/**
 * ConnectScreen: Tela de escaneamento de QR Code para pareamento com o Host.
 * Implementa o requisito FR-001 e FR-002.
 */
const ConnectScreen = ({ navigation }: any) => {
  const [isScanning, setIsScanning] = useState(true);

  const onQRCodeScan = (event: any) => {
    if (!isScanning) return;
    
    setIsScanning(false);
    const data = event.nativeEvent.codeStringValue;

    try {
      // Parse do JSON contido no QR Code gerado pelo Host
      const config = JSON.parse(data);
      
      if (config.ip && config.port) {
        // Tenta conectar ao Host Python
        SocketClient.connect(config.ip, config.port);
        
        // Navega para a tela de controle após conexão bem-sucedida
        Alert.alert('Sucesso', `Conectado ao Host: ${config.ip}`);
        navigation.navigate('MediaControls');
      } else {
        Alert.alert('Erro', 'Formato de QR Code inválido.');
        setIsScanning(true);
      }
    } catch (e) {
      Alert.alert('Erro', 'Não foi possível ler o QR Code.');
      setIsScanning(true);
    }
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Escanear QR Code do Host</Text>
      <CameraScreen
        showFrame={true}
        scanBarcode={true}
        onReadCode={onQRCodeScan}
        frameColor="white"
        colorForScannerFrame="red"
      />
      <View style={styles.footer}>
        <Button title="Voltar" onPress={() => navigation.goBack()} />
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: 'black' },
  title: { color: 'white', textAlign: 'center', margin: 20, fontSize: 18 },
  footer: { padding: 20 }
});

export default ConnectScreen;
