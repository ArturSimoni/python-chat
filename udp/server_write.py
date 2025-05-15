import socket
import json

def start_server(host: str, port: int):
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind((host, port))

    clients = set()

    print(f'Server (write) starting {host}:{port}\nListening now...')

    while True:
        try:
            data, addr = server.recvfrom(1024)
            data_cliente = json.loads(data.decode('utf-8'))

            message = data_cliente['message']
            sender = tuple(data_cliente['address'])

            print(f"[Mensagem recebida de {sender}]: {message}")

            clients.add(sender)

            for client in list(clients):
                if client != sender:  
                    try:
                        server.sendto(message.encode('utf-8'), client)
                    except Exception as e:
                        print(f"[Erro ao enviar para {client}]: {e}")
                        clients.remove(client) 
        except Exception as e:
            print(f"[Erro geral]: {e}")

if __name__ == '__main__':
    HOST = 'localhost'
    PORT = 8000

    start_server(HOST, PORT)