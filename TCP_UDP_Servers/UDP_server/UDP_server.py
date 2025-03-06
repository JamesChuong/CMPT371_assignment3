import socket
import sys

PORT = 53333
HOST = "127.0.0.1"

def main():
    UDP_MSG = "back at you UDP"

    UDP_Socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    UDP_Socket.bind((HOST, PORT))

    while True:

        msg, client = UDP_Socket.recvfrom(1024)
        UDP_Socket.sendto(UDP_MSG.encode(), client)
        print(msg)
        if msg.decode() == '1':
            print("Server and client terminated")
            break


if __name__ == '__main__':
    sys.exit(main())