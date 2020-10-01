"""
    created at sep 30/2020 by Mmd4LIFE
    - this package handle all client that connect
        to our server tcp
"""

from threading import Thread
from datetime import datetime
from json import dumps as json_dumps
from time import sleep

from .message_handler import MassageHandler


class ClientHandler(Thread):

    def __init__(self, client: object, client_address: object):
        Thread.__init__(self)

        self.client = client
        self.client_address = client_address

        self.firt_message = False

    def run(self):
        """ run new client thread from this functin
            :params:
            :return:
        """
        if self.firt_message is False:
            # send welcome message to server
            self.client.sendall(str(
                json_dumps({
                    "message" : "Welcome to Chat-App server",
                    "command" : "START",
                    "from" : "server",
                    "group" : "brodcast"
                })
            ).encode("utf-8"))
            sleep(.1)
            self.client.sendall(str(
                json_dumps({
                    "message" : "",
                    "command" : "AUTH",
                    "from" : "server",
                    "group" : "brodcast"
                })
            ).encode("utf-8"))
            self.firt_message = True

        MassageHandler(socket_client=self.client).start()

