import socket 

def send_message(message:str, host: str, port:int):
    server = socket.socket(socket.AF_INET, socket.SOCK.DGRAM)
    server.settimeout(1)
    
    server.sendto(message.encode(),(HOST, PORT))


if __name__=='_main__':

    HOST = 'localhost'
    PORT = 8000

    message = input('type your message')
    send_message(message, HOST, PORT)
   