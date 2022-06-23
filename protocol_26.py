"""
EX 2.6 protocol implementation
Author: Noam Cohen
Date: 26.11.2020
"""

import datetime
import random

LENGTH_FIELD_SIZE = 2
PORT = 8820
LOW = 1
HIGH = 10
CURRENT_TIME = "%X"
SERVER_NAME = "Noam_Server"


def check_cmd(data):
    """Check if the command is defined in the protocol (e.g RAND, NAME, TIME, EXIT)"""
    valid_cmd = ["TIME", "NAME", "RAND", "EXIT"]  # All valid commands
    # If data is a valid variable:
    if data in valid_cmd:
        return True
    # Else:
    return False


def create_msg(data):
    """Create a valid protocol message, with length field"""
    length = str(len(data))  # length of data as a str type
    zfill_length = length.zfill(LENGTH_FIELD_SIZE)  # make it with 2 digits
    return zfill_length + data


def get_msg(my_socket):
    """
    Extract message from protocol, without the length field
    If length field does not include a number, returns False, "Error"
    """
    # Receives length of message as a str type:
    length = my_socket.recv(LENGTH_FIELD_SIZE).decode()
    # if all characters in length are digits:
    if length.isdigit():
        # Receive the command:
        cmd = my_socket.recv(int(length)).decode()
        # Return 'True' to approve that we are good
        # and that command without the length
        return True, cmd
    # Else:
    return False, "Error"


def create_server_rsp(cmd):
    """Based on the command, create a proper response"""
    # If the user has entered "EXIT":
    if cmd == "EXIT":
        return "EXIT"
    # If the user has entered "TIME":
    if cmd == "TIME":
        # Then the current time will be returned
        current_time = datetime.datetime.now()
        return current_time.strftime(CURRENT_TIME)
    # If the user has entered "NAME":
    if cmd == "NAME":
        # Then the server name will be returned
        return SERVER_NAME
    # If the user has entered "RAND":
    if cmd == "RAND":
        # Then a random number (between 1 and 10) will be returned
        return str(random.randint(LOW, HIGH))
