"""
    created at oct 02/2020 by Mmd4LIFE
    - this package act as client socket command
"""

from json import (
    loads as json_loads,
    dumps as json_dumps
)
from datetime import datetime
from socket import socket

class MassageHandler:

    def __init__(self, socket_client: socket):
        super(MassageHandler, self).__init__()

        self.socket_client = socket_client

    def start(self):
        message: str = self.socket_client.recv(8096).decode("utf-8")
        data_json = json_loads(message)
        
        if data_json["command"] == "AUTH":
            username: str = data_json["message"]["username"]
            password: str = data_json["message"]["password"]
            print(username)
        #    del username, password

        #if message is None or message == "[EXIT]":
        #    self.socket_client.close()
        #    return

        #print("[+] client send message as: %s" % (message))

        del message

        self.start()
