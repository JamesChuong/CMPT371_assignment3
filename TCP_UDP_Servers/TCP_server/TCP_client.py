import socket
import sys
import time
import numpy as np

TCP_IP = '127.0.0.1'
TCP_PORT = 53333


def main():

    f = open("TCP_results.txt", "w")

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect((TCP_IP, TCP_PORT))
    TCP_msg = "hello TCP"

    # f.write("TCP Part 1: Sending a single message\n")
    #

    #
    # start = time.time()
    # server.sendall(TCP_msg.encode())
    # server_response = server.recv(1024)
    # end = time.time()
    #
    # f.write(f"The RTT is {(end-start)*1000} ms\n")

    f.write("TCP Part 2: Sending 1000 messages\n")

    start = time.time()
    for i in range(1000):

        server.sendall(TCP_msg.encode())
        server_response = server.recv(1024)
    end = time.time()

    stop = "1"
    server.sendall(stop.encode())
    server_response = server.recv(1024)

    if server_response.decode() == '2':
        print("Connection terminated")

    f.write(f"The RTT is {(end-start)*1000} ms\n")


if __name__ == '__main__':
    sys.exit(main())