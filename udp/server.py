import socket

def start_server(host: str, port: int):
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind((host, port))

    clients = set()
    
    print(f'Servidor iniciado em {host}:{port}\nEscutando agora...')

    while True:
        data, addr = server.recvfrom(1024)
        print(f'[CLIENTE] {addr}: {data.decode()}')

        if addr not in clients:
            clients.add(addr)
            print(f'Novo cliente conectado: {addr}')

        for client_addr in clients:
            server.sendto(data, client_addr)
            print(f'[SERVIDOR] Enviado para {client_addr}: {data.decode()}')

if __name__ == '__main__':
    HOST = 'localhost'
    PORT = 8000
    

    start_server(HOST, PORT)
