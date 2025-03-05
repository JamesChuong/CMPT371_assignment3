# CMPT371_assignment3

Using the programming language of your choice, write two sets of client-server programs. In
one set, the client and the server (on port 53333) communicate over TCP, with the client sending a “hello
TCP” message to the server, and the server replying with “back at you TCP”. In the other set, the same
operations are performed but over UDP (server on port 53444), and the messages are “Hello UDP” and “back
at you UDP. The client then computes and prints the RTT. RTT shall not include the time it takes to
construct a packet or extract data from it. You must use sockets directly; you cannot use any frameworks that
take care of sending/receiving data for you.
