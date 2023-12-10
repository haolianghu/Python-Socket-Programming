###############################################################################
# server-python.py
# Name: Haoliang Hu
# EID: hh27683
###############################################################################

import sys
import socket
import threading

# BUFF_SIZ_RECV will be used as the buffer size for recv() calls, the size is in bytes
BUFF_SIZ_RECV = 1234
# MAX_Q is the number of outstanding requests allowed
MAX_Q = 10

def handle_client(connection):
    """
    Handle client connection, where messages from a client are received and printed to sys.stdout
    """
    try:
        while True:
            # Receive data but limit the amount of data to receive at any one time
            data = connection.recv(BUFF_SIZ_RECV)
            # If data is received, output the data to sys.stdout to show in terminal
            if data:
                sys.stdout.write(data.decode())
            # If no more data is received break out of the loop so the code can move from the try block to the finally block
            else:
                break
                
    finally:
        connection.close()

def server(server_port):
    """
    Listen on socket and print received message to sys.stdout
    This is done with threads so that the server can handle multiple clients at the same time
    """
    # Create a TCP/IP socket 
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to server IP address and port
    server_address = ('127.0.0.1', server_port)
    sock.bind(server_address)

    # Listen for incoming connections
    # The argument to listen is the number of outstanding requests allowed
    sock.listen(MAX_Q)
    
    while True:
        # Accept a connection after hearing an incoming connection
        # The connection variable is a new socket object usable to send and receive data on the connection
        connection = sock.accept()[0]
        # Start a new thread to handle this client connection, such as sending and receiving data
        client_thread = threading.Thread(target=handle_client, args=(connection,))
        # .start() method will start a new thread and call the specified function with the specified arguments
        client_thread.start()

def main():
    """Parse command-line argument and call server function """
    # If the number of arguments is not 2, exit the program and tell the user the proper usage
    if len(sys.argv) != 2:
        sys.exit("Usage: python server-python.py [Server Port]")
    # The second argument is the server port
    server_port = int(sys.argv[1])
    server(server_port)

if __name__ == "__main__":
    main()

# python3 -u server-python.py 20000 > output.txt
# diff input.txt output.txt