import React, { useState, useEffect, useRef } from 'react';
import { View, Text, TextInput, FlatList, TouchableOpacity, StyleSheet, KeyboardAvoidingView, Platform } from 'react-native';
import SocketClient from '../services/socket_client';

/**
 * ChatComponent: Interface de comunicação em tempo real com o Host.
 * Implementa o requisito FR-011.
 */
const ChatComponent = () => {
  const [message, setMessage] = useState('');
  const [chatHistory, setChatHistory] = useState([]);
  const flatListRef = useRef(null);

  useEffect(() => {
    // Escuta novas mensagens vindas do Host ou de outros clientes
    const handleMessage = (msg: any) => {
      if (msg.type === 'CHAT_MSG') {
        setChatHistory((prev) => [...prev, {
          id: Date.now().toString() + Math.random(),
          sender: msg.payload.sender,
          content: msg.payload.content,
          time: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
        }]);
      }
    };

    SocketClient.on('message', handleMessage);
    return () => {
      SocketClient.removeListener('message', handleMessage);
    };
  }, []);

  const sendMessage = () => {
    if (!message.trim()) return;

    const payload = {
      type: 'CHAT_MSG',
      payload: {
        sender: 'Celular',
        content: message
      }
    };

    SocketClient.sendCommand(payload);
    
    // Adiciona localmente para feedback imediato (Optimistic UI)
    setChatHistory((prev) => [...prev, {
      id: Date.now().toString(),
      sender: 'Você',
      content: message,
      time: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
    }]);
    
    setMessage('');
  };

  return (
    <KeyboardAvoidingView 
      behavior={Platform.OS === 'ios' ? 'padding' : 'height'} 
      style={styles.container}
      keyboardVerticalOffset={100}
    >
      <FlatList
        ref={flatListRef}
        data={chatHistory}
        keyExtractor={(item) => item.id}
        renderItem={({ item }) => (
          <View style={[styles.messageBubble, item.sender === 'Você' ? styles.myMessage : styles.theirMessage]}>
            <Text style={styles.senderText}>{item.sender}</Text>
            <Text style={styles.messageText}>{item.content}</Text>
            <Text style={styles.timeText}>{item.time}</Text>
          </View>
        )}
        onContentSizeChange={() => flatListRef.current?.scrollToEnd()}
      />

      <View style={styles.inputContainer}>
        <TextInput
          style={styles.input}
          placeholder="Digite uma mensagem..."
          placeholderTextColor="#aaa"
          value={message}
          onChangeText={setMessage}
          onSubmitEditing={sendMessage}
        />
        <TouchableOpacity style={styles.sendButton} onPress={sendMessage}>
          <Text style={styles.sendButtonText}>Enviar</Text>
        </TouchableOpacity>
      </View>
    </KeyboardAvoidingView>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#1a1a1a' },
  messageBubble: { padding: 10, borderRadius: 10, margin: 5, maxWidth: '80%' },
  myMessage: { alignSelf: 'flex-end', backgroundColor: '#2ecc71' },
  theirMessage: { alignSelf: 'flex-start', backgroundColor: '#34495e' },
  senderText: { fontSize: 10, color: '#eee', marginBottom: 2 },
  messageText: { color: 'white', fontSize: 14 },
  timeText: { fontSize: 8, color: '#ddd', alignSelf: 'flex-end', marginTop: 2 },
  inputContainer: { flexDirection: 'row', padding: 10, backgroundColor: '#2c3e50' },
  input: { flex: 1, backgroundColor: '#34495e', color: 'white', paddingHorizontal: 15, borderRadius: 20, height: 40 },
  sendButton: { marginLeft: 10, justifyContent: 'center', backgroundColor: '#3498db', paddingHorizontal: 15, borderRadius: 20 },
  sendButtonText: { color: 'white', fontWeight: 'bold' }
});

export default ChatComponent;
