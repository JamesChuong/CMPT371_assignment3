import socket
import sys

PORT = 53444
HOST = "127.0.0.1"
UDP_MSG = "back at you UDP"

def main():

    UDP_Socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    UDP_Socket.bind((HOST, PORT))

    while True:

        msg, client = UDP_Socket.recvfrom(1024)
        UDP_Socket.sendto(UDP_MSG.encode(), client)

if __name__ == '__main__':
    sys.exit(main())