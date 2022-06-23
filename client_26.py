"""
EX 2.6 client implementation
Author: Noam Cohen
Date: 26.11.2020
"""


import socket
import protocol_26


def main():
    # Open socket with the server:
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_socket.connect(("127.0.0.1", protocol_26.PORT))

    while True:
        user_input = input("Enter command\n")
        # Check if user entered a valid command as defined in protocol
        valid_cmd = protocol_26.check_cmd(user_input)

        # If the command is valid:
        if valid_cmd:
            # 1. Add length field ("RAND" -> "04RAND")
            data = protocol_26.create_msg(user_input)
            # 2. Send it to the server
            my_socket.send(data.encode())
            # 3. If command is EXIT:
            if data[protocol_26.LENGTH_FIELD_SIZE:] == "EXIT":
                # Then break from while loop
                break
            # 4. Get server's response
            # valid_size is a boolean value that check if server's response is valid
            # and server_rsp including the server's response
            (valid_size, server_rsp) = protocol_26.get_msg(my_socket)
            # 5. If server's response is valid:
            if valid_size:
                # Then print it:
                print(server_rsp)
            # If size of the server response is not valid:
            else:
                print("Response not valid\n")
        # If user_input is not valid:
        else:
            print("Not a valid command")

    print("Closing\n")
    # Close socket
    my_socket.close()


if __name__ == "__main__":
    main()
