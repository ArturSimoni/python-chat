import socket

def send_message(host: str, port: int):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.settimeout(1) 

    while True:
        message = input('Digite sua mensagem: ')
        
        client_socket.sendto(message.encode(), (host, port))

        try:

            data, addr = client_socket.recvfrom(1024)
            print(f'[Mensagem recebida]: {data.decode()}')
        except socket.timeout:
            print("[Erro]: Tempo limite atingido. Nenhuma resposta do servidor.")

if __name__ == '__main__':
    HOST = 'localhost'
    PORT = 8000

    send_message(HOST, PORT)
