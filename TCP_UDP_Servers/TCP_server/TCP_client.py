import socket
import sys
import time

TCP_IP = '127.0.0.1'
TCP_PORT = 53333


def main():

    TCP_msg = "hello TCP"
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect((TCP_IP, TCP_PORT))

    start = time.time()
    server.sendall(TCP_msg.encode())
    server_response = server.recv(1024)
    end = time.time()
    print(f"The RTT is {(end-start)*1000:.2f} ms")

if __name__ == '__main__':
    sys.exit(main())