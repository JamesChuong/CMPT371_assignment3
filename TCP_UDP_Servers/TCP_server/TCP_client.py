import socket
import sys
import time

TCP_IP = '127.0.0.1'
TCP_PORT = 53333


def main():

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect((TCP_IP, TCP_PORT))
    TCP_msg = "hello TCP"

    start = time.perf_counter_ns()
    server.sendall(TCP_msg.encode())
    server_response = server.recv(1024)
    end = time.perf_counter_ns()

    print(f"The RTT is {(end-start)} nanoseconds")

    # Sending 1000 messages
    start = time.perf_counter_ns()
    for i in range(1000):

        server.sendall(TCP_msg.encode())
        server_response = server.recv(1024)
    end = time.perf_counter_ns()

    print(f"The total time is {(end-start)} nanoseconds")

    stop = "1"
    server.sendall(stop.encode())
    server_response = server.recv(1024)


if __name__ == '__main__':
    sys.exit(main())