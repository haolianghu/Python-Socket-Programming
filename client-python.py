###############################################################################
# client-python.py
# Name: Haoliang Hu
# EID: hh27683
###############################################################################

import sys
import socket

def client(server_ip, server_port):
    """Open socket and send message from sys.stdin"""
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the server IP address and port 
    server_address = (server_ip, server_port)
    sock.connect(server_address)

    try:
        # Send data by reading from sys.stdin
        message = sys.stdin.read()
        # Send the message in chunks, where each chunk is in bytes
        chunk_size = 123
        for i in range(0, len(message), chunk_size):
            # convert string message to bytes use encode()
            # this will return a bytes object that can be sent over the network using a socket
            sock.sendall(message[i:i+chunk_size].encode())

    finally:
        # Let user know which server it is closing the connection to
        # {!r} is used to print the repr() of the data, which is the string representation of the data, it is also a placeholder
        # Format is used to fill in the placeholder with the data
        sys.stdout.write('closing socket to {!r}\n'.format(server_address))
        sock.close()

def main():
    """Parse command-line arguments and call client function """
    # Check for the correct number of arguments
    if len(sys.argv) != 3:
        # If the number of arguments is not 3, exit the program and tell the user the proper usage
        sys.exit("Usage: python client-python.py [Server IP] [Server Port] < [message]")
    # The second argument is the server IP
    server_ip = sys.argv[1]
    # The third argument is the server port
    server_port = int(sys.argv[2])
    client(server_ip, server_port)

if __name__ == "__main__":
    main()

# python3 client-python.py 127.0.0.1 20000 < input.txt 
# diff input.txt output.txt