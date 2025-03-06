import socket
import sys
import time

PORT = 53444
HOST = '127.0.0.1'


def main():

    f = open("UDP_results.txt", "w")

    UDP_MSG = "Hello UDP"
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # f.write("UDP Part 1: Sending a single message\n")
    #
    # start = time.time()
    # server.sendto(UDP_MSG.encode(), (HOST, PORT))
    # server_response, _ = server.recvfrom(1024)
    # end = time.time()
    #
    # f.write(f"The RTT is {(end-start)*1000} ms\n")

    f.write("UDP Part 2: Sending 1000 messages\n")

    start = time.time()

    for i in range(1000):

        server.sendto(UDP_MSG.encode(), (HOST, PORT))
        server_response, _ = server.recvfrom(1024)

    end = time.time()

    f.write(f"The RTT is {(end-start)*1000} ms\n")

    kill_msg = '1'
    server.sendto(kill_msg.encode(), (HOST, PORT))

if __name__ == '__main__':
    sys.exit(main())