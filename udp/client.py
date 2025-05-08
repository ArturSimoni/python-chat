import socket 

def send_message(message:str, host: str, port:int):
    server = socket.socket(socket.AF_INET, socket.SOCK.DGRAM)
    server.settimeout(1)

    while True:
        message = input('type your message')
        server.sendto(message.encode(),(HOST, PORT))

        data, addr = server.recvfrom(1024)
        print(f'[Message]: {data.decode()}')


if __name__=='_main__':

    HOST = 'localhost'
    PORT = 8000

    
    send_message(HOST, PORT)
   