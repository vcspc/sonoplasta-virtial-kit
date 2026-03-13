import React from 'react';
import { View, Text, TouchableOpacity, StyleSheet, Dimensions } from 'react-native';
import SocketClient from '../services/socket_client';

/**
 * MediaControls: Painel de botões para controle remoto de áudio, vídeo e slides.
 * Implementa o requisito FR-003, FR-004 e FR-005.
 */
const MediaControls = ({ navigation }: any) => {
  
  const sendVlcCommand = (action: string) => {
    const command = {
      id: Date.now().toString(),
      type: 'VLC_CMD',
      payload: { action }
    };
    SocketClient.sendCommand(command);
  };

  const sendSlideCommand = (action: string) => {
    const command = {
      id: Date.now().toString(),
      type: 'SLIDE_CMD',
      payload: { action }
    };
    SocketClient.sendCommand(command);
  };

  return (
    <View style={styles.container}>
      <Text style={styles.header}>Controle de Mídia VLC</Text>
      
      {/* Grupo VLC */}
      <View style={styles.row}>
        <ControlButton label="VOL -" onPress={() => sendVlcCommand('VOL_DOWN')} color="#f39c12" />
        <ControlButton label="PLAY/PAUSE" onPress={() => sendVlcCommand('PLAY')} color="#2ecc71" flex={2} />
        <ControlButton label="VOL +" onPress={() => sendVlcCommand('VOL_UP')} color="#f39c12" />
      </View>

      <View style={styles.row}>
        <ControlButton label="FULLSCREEN" onPress={() => sendVlcCommand('FULLSCREEN')} color="#3498db" />
        <ControlButton label="STOP" onPress={() => sendVlcCommand('STOP')} color="#e74c3c" />
      </View>

      <View style={styles.separator} />

      {/* Grupo Slides */}
      <Text style={styles.header}>Controle de Slides</Text>
      <View style={styles.row}>
        <ControlButton label="ANTERIOR" onPress={() => sendSlideCommand('PREV')} color="#9b59b6" />
        <ControlButton label="PRÓXIMO" onPress={() => sendSlideCommand('NEXT')} color="#9b59b6" />
      </View>

      <View style={styles.separator} />

      {/* Janelas */}
      <View style={styles.row}>
        <ControlButton label="FECHAR JANELA (ALT+F4)" onPress={() => sendVlcCommand('CLOSE_WINDOW')} color="#34495e" />
      </View>
    </View>
  );
};

// Componente de botão reutilizável interno
const ControlButton = ({ label, onPress, color, flex = 1 }: any) => (
  <TouchableOpacity 
    onPress={onPress} 
    style={[styles.button, { backgroundColor: color, flex }]}
    activeOpacity={0.7}
  >
    <Text style={styles.buttonText}>{label}</Text>
  </TouchableOpacity>
);

const { width } = Dimensions.get('window');

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#1a1a1a', padding: 15, justifyContent: 'center' },
  header: { color: '#ecf0f1', fontSize: 20, fontWeight: 'bold', marginBottom: 20, textAlign: 'center' },
  row: { flexDirection: 'row', justifyContent: 'space-around', marginBottom: 15 },
  button: {
    paddingVertical: 20,
    marginHorizontal: 5,
    borderRadius: 10,
    alignItems: 'center',
    justifyContent: 'center',
    elevation: 5,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.25,
    shadowRadius: 3.84,
  },
  buttonText: { color: 'white', fontSize: 14, fontWeight: 'bold', textAlign: 'center' },
  separator: { height: 1, backgroundColor: '#333', marginVertical: 25 }
});

export default MediaControls;
