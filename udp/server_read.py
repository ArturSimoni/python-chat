import socket
import json

def start_server(host_read: str, port_read: int, host_write: str, port_write: int):
    server_read = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_read.bind((host_read, port_read))

    print(f'Server (read) starting {host_read}:{port_read}\nListening now...')

    server_write = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        try:
            data, addr = server_read.recvfrom(1024)
            message = data.decode('utf-8')

            print(f"[Mensagem recebida de {addr}]: {message}")

            data_cliente = {
                'message': message,
                'address': addr
            }
            data_cliente_json = json.dumps(data_cliente).encode('utf-8')

            server_write.sendto(data_cliente_json, (host_write, port_write))

        except Exception as e:
            print(f"[Erro]: {e}")

if __name__ == '__main__':
    HOST_READ = 'localhost'
    PORT_READ = 9000

    HOST_WRITE = 'localhost'
    PORT_WRITE = 8000

    start_server(HOST_READ, PORT_READ, HOST_WRITE, PORT_WRITE)