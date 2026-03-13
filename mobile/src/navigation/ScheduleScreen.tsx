import React, { useState, useEffect } from 'react';
import { View, Text, FlatList, TouchableOpacity, StyleSheet, SectionList } from 'react-native';
import SocketClient from '../services/socket_client';

/**
 * ScheduleScreen: Tela de organização do roteiro e busca de arquivos locais.
 * Implementa o requisito FR-010 e FR-013.
 */
const ScheduleScreen = () => {
  const [localFiles, setLocalFiles] = useState([]);
  const [scheduleItems, setScheduleItems] = useState([]);

  useEffect(() => {
    // Solicita dados iniciais ao Host
    SocketClient.sendCommand({ type: 'FILE_SEARCH', payload: {} });
    SocketClient.sendCommand({ type: 'SCHEDULE_GET', payload: {} });

    const handleMessage = (message: any) => {
      if (message.type === 'FILE_SEARCH_RESULTS') {
        setLocalFiles(message.payload.files);
      } else if (message.type === 'SCHEDULE_DATA') {
        setScheduleItems(message.payload.items);
      }
    };

    SocketClient.on('message', handleMessage);
    return () => {
      SocketClient.removeListener('message', handleMessage);
    };
  }, []);

  const openOnHost = (path: string) => {
    SocketClient.sendCommand({
      type: 'FILE_OPEN',
      payload: { path }
    });
  };

  const addToSchedule = (item: any) => {
    SocketClient.sendCommand({
      type: 'SCHEDULE_ADD',
      payload: { item }
    });
  };

  return (
    <View style={styles.container}>
      <Text style={styles.header}>Cronograma do Culto</Text>
      <FlatList
        data={scheduleItems}
        keyExtractor={(item: any) => item.id}
        style={styles.scheduleList}
        renderItem={({ item }) => (
          <TouchableOpacity style={styles.scheduleItem} onPress={() => openOnHost(item.path)}>
            <Text style={styles.itemText}>{item.title}</Text>
            <Text style={styles.itemType}>{item.type}</Text>
          </TouchableOpacity>
        )}
        ListEmptyComponent={<Text style={styles.empty}>Cronograma vazio</Text>}
      />

      <View style={styles.divider} />

      <Text style={styles.header}>Arquivos no PC (Host)</Text>
      <FlatList
        data={localFiles}
        keyExtractor={(item: any) => item.path}
        renderItem={({ item }) => (
          <View style={styles.fileItem}>
            <View style={{ flex: 1 }}>
              <Text style={styles.itemText} numberOfLines={1}>{item.title}</Text>
            </View>
            <View style={styles.fileActions}>
              <TouchableOpacity style={styles.actionBtn} onPress={() => openOnHost(item.path)}>
                <Text style={styles.btnText}>ABRIR</Text>
              </TouchableOpacity>
              <TouchableOpacity style={[styles.actionBtn, { backgroundColor: '#3498db' }]} onPress={() => addToSchedule(item)}>
                <Text style={styles.btnText}>+</Text>
              </TouchableOpacity>
            </View>
          </View>
        )}
      />
    </View>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#1a1a1a', padding: 10 },
  header: { color: '#f1c40f', fontSize: 18, fontWeight: 'bold', marginVertical: 10 },
  scheduleList: { maxHeight: '40%' },
  scheduleItem: { backgroundColor: '#2c3e50', padding: 12, borderRadius: 5, marginBottom: 5, flexDirection: 'row', justifyContent: 'space-between' },
  fileItem: { backgroundColor: '#333', padding: 12, borderRadius: 5, marginBottom: 5, flexDirection: 'row', alignItems: 'center' },
  itemText: { color: 'white', fontSize: 14 },
  itemType: { color: '#888', fontSize: 10 },
  divider: { height: 2, backgroundColor: '#444', marginVertical: 15 },
  empty: { color: '#666', textAlign: 'center', marginTop: 10 },
  fileActions: { flexDirection: 'row' },
  actionBtn: { backgroundColor: '#2ecc71', padding: 8, borderRadius: 4, marginLeft: 10 },
  btnText: { color: 'white', fontWeight: 'bold', fontSize: 12 }
});

export default ScheduleScreen;
