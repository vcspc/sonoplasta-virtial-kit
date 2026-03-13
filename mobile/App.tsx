import React from 'react';
import { View, TouchableOpacity, Text } from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import ConnectScreen from './src/navigation/ConnectScreen';
import MediaControls from './src/components/MediaControls';
import YoutubeSearch from './src/components/YoutubeSearch';
import ScheduleScreen from './src/navigation/ScheduleScreen';
import ChatComponent from './src/components/ChatComponent';
import FileTransfer from './src/components/FileTransfer';

/**
 * App: Componente raiz que define a navegação do sistema Sonoplasta Virtual Kit.
 */
const Stack = createStackNavigator();

const App = () => {
  return (
    <NavigationContainer>
      <Stack.Navigator 
        initialRouteName="Connect"
        screenOptions={{
          headerStyle: { backgroundColor: '#2c3e50' },
          headerTintColor: '#fff',
          headerTitleStyle: { fontWeight: 'bold' },
        }}
      >
        <Stack.Screen 
          name="Connect" 
          component={ConnectScreen} 
          options={{ title: 'Parear Dispositivo' }} 
        />
        <Stack.Screen 
          name="MediaControls" 
          component={MediaControls} 
          options={{ 
            title: 'Painel de Controle',
            headerRight: () => <HeaderIcons />
          }} 
        />
        <Stack.Screen 
          name="YoutubeSearch" 
          component={YoutubeSearch} 
          options={{ title: 'Buscar no YouTube' }} 
        />
        <Stack.Screen 
          name="Schedule" 
          component={ScheduleScreen} 
          options={{ title: 'Cronograma do Culto' }} 
        />
        <Stack.Screen 
          name="Chat" 
          component={ChatComponent} 
          options={{ title: 'Chat com o Host' }} 
        />
        <Stack.Screen 
          name="FileTransfer" 
          component={FileTransfer} 
          options={{ title: 'Transferir Arquivos' }} 
        />
      </Stack.Navigator>
    </NavigationContainer>
  );
};

/**
 * HeaderIcons: Helper para exibir os botões de navegação rápida no topo.
 */
const HeaderIcons = () => {
  const navigation = require('@react-navigation/native').useNavigation();
  
  return (
    <View style={{ flexDirection: 'row', marginRight: 10 }}>
      <TouchableOpacity 
        onPress={() => navigation.navigate('YoutubeSearch')}
        style={{ marginRight: 12 }}
      >
        <Text style={{ color: 'white', fontWeight: 'bold', fontSize: 10 }}>YOUTUBE</Text>
      </TouchableOpacity>
      <TouchableOpacity 
        onPress={() => navigation.navigate('Schedule')}
        style={{ marginRight: 12 }}
      >
        <Text style={{ color: '#f1c40f', fontWeight: 'bold', fontSize: 10 }}>CRONO</Text>
      </TouchableOpacity>
      <TouchableOpacity 
        onPress={() => navigation.navigate('Chat')}
        style={{ marginRight: 12 }}
      >
        <Text style={{ color: '#2ecc71', fontWeight: 'bold', fontSize: 10 }}>CHAT</Text>
      </TouchableOpacity>
      <TouchableOpacity 
        onPress={() => navigation.navigate('FileTransfer')}
      >
        <Text style={{ color: '#3498db', fontWeight: 'bold', fontSize: 10 }}>FILES</Text>
      </TouchableOpacity>
    </View>
  );
};

export default App;
