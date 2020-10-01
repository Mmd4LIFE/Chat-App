"""
    created at oct 02/2020 by Mmd4LIFE
    - this package act as client socket command
"""

from socket import socket
from json import (
    loads as json_loads,
    dumps as json_dumps
)
from datetime import datetime

#from ChatAppCLient.src.commons.constants.colors import Colors
from commons.constants.colors import Colors

class CommandHandler:

    def __init__(self, client_socket: socket):
        super(CommandHandler, self).__init__()

        self.client_socket = client_socket
        self.username: str = None
        #self.password: str = None

    def start(self):
        """ start command handler service
        :params:
        :return:
        """

        message: str = self.client_socket.recv(8096).decode("utf-8")

        json_data: dict = json_loads(message)

        if json_data["command"] == "START":
            print(
                Colors.FORE_GREEN + "[+] connecting to ChatApp server was successfully ..."
            )

            print(
                Colors.FORE_CYAN + str(datetime.now()).split('.')[0] +
                " => " + json_data["from"] + ":: " + json_data["message"]
            )
        elif json_data["command"] == "AUTH":
            print("#" * 10 + "AUTHENTICATION" + "#" * 10)
            username: str = input("Enter your username:: ")
            password: str = input("Enter your password:: ")

            self.client_socket.sendall(str(
                json_dumps({
                    "message" : {
                        "username": username,
                        "password": password
                    },
                    "command": "START",
                    "from": "client",
                    "group": "server"
                })
            ).encode("utf-8"))

            del username, password

        self.start()
