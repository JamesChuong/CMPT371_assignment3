import socket
import sys

HOST = '127.0.0.1'
PORT = 53333


def main():

    TCP_msg = 'back at you TCP'

    TCP_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    TCP_socket.bind((HOST, PORT))
    TCP_socket.listen()
    client_socket, client_address = TCP_socket.accept()

    while True:

        client_msg = client_socket.recv(1024)
        client_socket.sendall(TCP_msg.encode())
        if client_msg.decode() == '1':
            acknowledgment = '2'
            client_socket.sendall(acknowledgment.encode())
            client_socket.close()
            break


if __name__ == '__main__':
        sys.exit(main())