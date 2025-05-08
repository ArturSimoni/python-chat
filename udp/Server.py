from http import client
import socket 

def start_server(message:str, host: str, port:int):
    server = socket.socket(socket.AF_INET, socket.SOCK.DGRAM)

    server.bind((host,port))
    print(f'server started at {host}:{port}\n Listening now')
    while True:
        data, addr = server.recvfrom(1024)
        print(f'[CLIENTE] {addr}: {data.decode()}')
        if addr not in client:
            client.add(addr)

            for client in client:
                server.sendto(data,client)
                print(f'[SERVER]: {data.decode()}')

if __name__=='_main__':

    HOST = 'localhost'
    PORT = 8000

    start_server( HOST, PORT)
   