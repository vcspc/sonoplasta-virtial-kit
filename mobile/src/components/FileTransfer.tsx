import React, { useState } from 'react';
import { View, Text, TextInput, TouchableOpacity, StyleSheet, Alert, ActivityIndicator } from 'react-native';
import SocketClient from '../services/socket_client';

/**
 * FileTransfer: Interface para envio de arquivos com autenticação.
 * Implementa o requisito FR-009.
 */
const FileTransfer = () => {
  const [password, setPassword] = useState('');
  const [isUploading, setIsUploading] = useState(false);

  const startTransfer = () => {
    if (!password) {
      Alert.alert('Erro', 'Informe a senha de transferência definida no Host.');
      return;
    }

    setIsUploading(true);

    // Mock de arquivo para demonstração do protocolo
    // Em produção, aqui seria usado react-native-document-picker para obter o arquivo real
    const fileMock = {
      filename: "apresentacao_culto.mp4",
      size: 5000000, // 5MB
      data: "binary_content_placeholder" 
    };

    const command = {
      type: 'FILE_XFER_START',
      payload: {
        filename: fileMock.filename,
        size: fileMock.size,
        password: password
      }
    };

    SocketClient.sendCommand(command);

    // Escuta a resposta do Host para a transferência
    const handleResponse = (msg: any) => {
      if (msg.type === 'READY_FOR_DATA') {
        // O Host está pronto. Aqui o binário seria enviado em chunks.
        Alert.alert('Transferência', 'Host autorizou o envio. Iniciando upload...');
        // Simulação de progresso...
        setTimeout(() => {
          setIsUploading(false);
          Alert.alert('Sucesso', 'Arquivo enviado com sucesso!');
        }, 2000);
      } else if (msg.type === 'ERROR') {
        setIsUploading(false);
        Alert.alert('Erro', msg.payload);
      }
      SocketClient.removeListener('message', handleResponse);
    };

    SocketClient.on('message', handleResponse);
  };

  return (
    <View style={styles.container}>
      <Text style={styles.header}>Transferir Arquivo para o PC</Text>
      <Text style={styles.info}>O arquivo será salvo na pasta 'media' do Host.</Text>
      
      <View style={styles.card}>
        <TextInput
          style={styles.input}
          placeholder="Senha de Transferência"
          placeholderTextColor="#888"
          secureTextEntry
          value={password}
          onChangeText={setPassword}
        />
        
        {isUploading ? (
          <ActivityIndicator size="large" color="#3498db" />
        ) : (
          <TouchableOpacity style={styles.uploadBtn} onPress={startTransfer}>
            <Text style={styles.btnText}>SELECIONAR E ENVIAR</Text>
          </TouchableOpacity>
        )}
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#1a1a1a', padding: 20, justifyContent: 'center' },
  header: { color: 'white', fontSize: 20, fontWeight: 'bold', textAlign: 'center', marginBottom: 10 },
  info: { color: '#888', textAlign: 'center', marginBottom: 30 },
  card: { backgroundColor: '#2c3e50', padding: 20, borderRadius: 10, elevation: 5 },
  input: { backgroundColor: '#34495e', color: 'white', padding: 12, borderRadius: 5, marginBottom: 20 },
  uploadBtn: { backgroundColor: '#3498db', padding: 15, borderRadius: 5, alignItems: 'center' },
  btnText: { color: 'white', fontWeight: 'bold' }
});

export default FileTransfer;
