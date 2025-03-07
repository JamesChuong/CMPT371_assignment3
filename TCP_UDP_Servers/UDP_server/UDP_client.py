import socket
import sys
import time

PORT = 53444
HOST = '127.0.0.1'


def main():

    UDP_MSG = "Hello UDP"
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # start = time.perf_counter_ns()
    # server.sendto(UDP_MSG.encode(), (HOST, PORT))
    # server_response, _ = server.recvfrom(1024)
    # end = time.perf_counter_ns()
    #
    # print(f"The RTT is {(end-start)} nanoseconds")


    start = time.perf_counter_ns()

    for i in range(1000):

        server.sendto(UDP_MSG.encode(), (HOST, PORT))
        server_response, _ = server.recvfrom(1024)

    end = time.perf_counter_ns()

    print(f"The total time is {(end-start)} nanoseconds")

    kill_msg = '1'
    server.sendto(kill_msg.encode(), (HOST, PORT))

if __name__ == '__main__':
    sys.exit(main())