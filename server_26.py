"""
EX 2.6 server implementation
Author: Noam Cohen
Date: 26.11.2020
"""

import socket
import protocol_26


def main():
    # Open socket with the client:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("0.0.0.0", protocol_26.PORT))
    server_socket.listen()
    print("Server is up and running")

    (client_socket, client_address) = server_socket.accept()
    print("Client connected")

    while True:
        # Get message from socket and check if it is according to protocol
        (valid_msg, cmd) = protocol_26.get_msg(client_socket)
        # If it is according to protocol:
        if valid_msg:
            # 1. Print received message
            print("Client sent: " + cmd)
            # 2. Check if the command is valid
            valid_cmd = protocol_26.check_cmd(cmd)
            # 3. If valid command - create response
            if valid_cmd:
                rsp = protocol_26.create_server_rsp(cmd)
            else:
                rsp = "Wrong command"
        # Else if it is not according to protocol:
        else:
            rsp = "Wrong protocol"
            # Attempt to empty the socket from possible garbage
            client_socket.recv(1024)
        # Handle EXIT command, no need to respond to the client
        if rsp == "EXIT":
            break        # Send response to the client
        reply = protocol_26.create_msg(rsp)
        client_socket.send(reply.encode())

    print("Closing\n")
    # Close sockets
    client_socket.close()
    server_socket.close()


if __name__ == "__main__":
    main()
