import TcpSocket from 'react-native-tcp-socket';
import { EventEmitter } from 'events';

/**
 * SocketClient: Gerencia a conexão TCP com o Host Python.
 * Implementa o protocolo JSON definido em contracts/socket-protocol.md.
 */
class SocketClient extends EventEmitter {
  private client: any = null;
  private isConnected: boolean = false;
  private buffer: string = '';

  constructor() {
    super();
  }

  /**
   * Conecta ao Host pelo IP e porta.
   * Input: host (string), port (number)
   */
  connect(host: string, port: number = 5000) {
    if (this.client) {
      this.disconnect();
    }

    const options = {
      port,
      host,
      localAddress: '127.0.0.1',
      reuseAddress: true,
    };

    this.client = TcpSocket.createConnection(options, () => {
      this.isConnected = true;
      this.emit('connected', { host, port });
      console.log(`Conectado ao Host: ${host}:${port}`);
    });

    this.client.on('data', (data: any) => {
      // Processa os dados recebidos acumulando no buffer
      this.buffer += data.toString();
      
      // Divide por nova linha conforme o contrato
      while (this.buffer.includes('\n')) {
        const parts = this.buffer.split('\n');
        const line = parts.shift();
        this.buffer = parts.join('\n');

        if (line && line.trim()) {
          try {
            const message = JSON.parse(line);
            this.emit('message', message);
            console.log(`Mensagem recebida do Host: ${message.type}`);
          } catch (e) {
            console.warn('Erro ao processar JSON do Host', e);
          }
        }
      }
    });

    this.client.on('error', (error: any) => {
      this.emit('error', error);
      console.error('Erro no Socket Client:', error);
    });

    this.client.on('close', () => {
      this.isConnected = false;
      this.emit('disconnected');
      console.log('Conexão encerrada com o Host');
    });
  }

  /**
   * Envia um comando JSON para o Host.
   * Input: command (object)
   */
  sendCommand(command: object) {
    if (this.client && this.isConnected) {
      try {
        const payload = JSON.stringify(command) + '\n';
        this.client.write(payload);
        console.log(`Comando enviado: ${(command as any).type}`);
      } catch (e) {
        console.error('Erro ao enviar comando:', e);
      }
    } else {
      console.warn('Socket não conectado. Impossível enviar comando.');
    }
  }

  /**
   * Encerra a conexão.
   */
  disconnect() {
    if (this.client) {
      this.client.destroy();
      this.client = null;
      this.isConnected = false;
    }
  }

  getStatus() {
    return this.isConnected;
  }
}

// Exporta uma única instância para o aplicativo (Singleton)
export default new SocketClient();
