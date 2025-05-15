import socket
import threading

def receive_messages(client_socket):
    """Função para receber mensagens do servidor."""
    while True:
        try:
            data, _addr = client_socket.recvfrom(1024)
            print(f'[Mensagem recebida]: {data.decode()}')
        except socket.timeout:
            continue
        except Exception as e:
            print(f"[Erro ao receber mensagem]: {e}")
            break

def send_message(host: str, port: int):
    """Função principal para enviar mensagens."""
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.settimeout(1)

    threading.Thread(target=receive_messages, args=(client_socket,), daemon=True).start()

    while True:
        try:
            message = input('Digite sua mensagem: ')
            client_socket.sendto(message.encode(), (host, port))
        except Exception as e:
            print(f"[Erro ao enviar mensagem]: {e}")
            break

if __name__ == '__main__':
    HOST = 'localhost'
    PORT = 9000  

    send_message(HOST, PORT)