import socket
import sys
import time

PORT = 53444
HOST = '127.0.0.1'


def main():

    UDP_MSG = "Hello UDP"

    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    start = time.time()
    server.sendto(UDP_MSG.encode(), (HOST, PORT))
    server_response, _ = server.recvfrom(1024)
    end = time.time()

    print(f"The RTT is {(end-start)*1000} ms")

if __name__ == '__main__':
    sys.exit(main())