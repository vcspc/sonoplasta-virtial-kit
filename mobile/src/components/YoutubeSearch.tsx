import React, { useState, useEffect } from 'react';
import { View, Text, TextInput, FlatList, TouchableOpacity, StyleSheet, ActivityIndicator } from 'react-native';
import SocketClient from '../services/socket_client';

/**
 * YoutubeSearch: Componente para buscar, projetar e baixar vídeos do YouTube.
 * Implementa os requisitos FR-006, FR-007 e FR-008.
 */
const YoutubeSearch = () => {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    // Escuta os resultados da busca vindos do Host
    const handleMessage = (message: any) => {
      if (message.type === 'YT_SEARCH_RESULTS') {
        setResults(message.payload.results);
        setLoading(false);
      }
    };

    SocketClient.on('message', handleMessage);
    return () => {
      SocketClient.removeListener('message', handleMessage);
    };
  }, []);

  const searchOnHost = () => {
    if (!query) return;
    setLoading(true);
    SocketClient.sendCommand({
      type: 'YT_SEARCH',
      payload: { query }
    });
  };

  const projectOnHost = (url: string) => {
    SocketClient.sendCommand({
      type: 'YT_OPEN',
      payload: { url }
    });
  };

  const downloadOnHost = (url: string, mode: string) => {
    SocketClient.sendCommand({
      type: 'YT_DOWNLOAD',
      payload: { url, mode }
    });
  };

  return (
    <View style={styles.container}>
      <View style={styles.searchBar}>
        <TextInput
          style={styles.input}
          placeholder="Buscar no YouTube..."
          placeholderTextColor="#888"
          value={query}
          onChangeText={setQuery}
          onSubmitEditing={searchOnHost}
        />
        <TouchableOpacity style={styles.searchButton} onPress={searchOnHost}>
          <Text style={styles.buttonText}>Lupa</Text>
        </TouchableOpacity>
      </View>

      {loading && <ActivityIndicator size="large" color="#e74c3c" style={{ marginTop: 20 }} />}

      <FlatList
        data={results}
        keyExtractor={(item: any) => item.id}
        renderItem={({ item }) => (
          <View style={styles.resultItem}>
            <Text style={styles.videoTitle} numberOfLines={2}>{item.title}</Text>
            <View style={styles.actions}>
              <TouchableOpacity style={styles.playButton} onPress={() => projectOnHost(item.url)}>
                <Text style={styles.actionText}>PROJETAR</Text>
              </TouchableOpacity>
              <TouchableOpacity style={styles.dlButton} onPress={() => downloadOnHost(item.url, 'VIDEO_AND_AUDIO')}>
                <Text style={styles.actionText}>BAIXAR</Text>
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
  searchBar: { flexDirection: 'row', marginBottom: 20 },
  input: { flex: 1, backgroundColor: '#333', color: 'white', padding: 10, borderRadius: 5 },
  searchButton: { backgroundColor: '#e74c3c', padding: 10, marginLeft: 10, borderRadius: 5, justifyContent: 'center' },
  buttonText: { color: 'white', fontWeight: 'bold' },
  resultItem: { backgroundColor: '#2c3e50', padding: 15, borderRadius: 10, marginBottom: 10 },
  videoTitle: { color: 'white', fontWeight: 'bold', marginBottom: 10 },
  actions: { flexDirection: 'row', justifyContent: 'space-between' },
  playButton: { backgroundColor: '#2ecc71', padding: 8, borderRadius: 5, flex: 1, marginRight: 5, alignItems: 'center' },
  dlButton: { backgroundColor: '#3498db', padding: 8, borderRadius: 5, flex: 1, marginLeft: 5, alignItems: 'center' },
  actionText: { color: 'white', fontSize: 12, fontWeight: 'bold' }
});

export default YoutubeSearch;
