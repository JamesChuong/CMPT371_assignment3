import socket
import sys

HOST = '127.0.0.1'
PORT = 53333


def main():

    TCP_msg = 'back at you TCP'

    TCP_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    TCP_socket.bind((HOST, PORT))
    TCP_socket.listen()

    while True:

        client_socket, client_address = TCP_socket.accept()
        client_msg = client_socket.recv(1024)
        client_socket.sendall(TCP_msg.encode())
        client_socket.close()


if __name__ == '__main__':
        sys.exit(main())