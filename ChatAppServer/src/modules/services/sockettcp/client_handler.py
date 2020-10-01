"""
    created at sep 30/2020 by Mmd4LIFE
    - this package handle all client that connect
        to our server tcp
"""

from threading import Thread
from datetime import datetime
from json import dumps as json_dumps


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
                    "command" : "START"
                })
            ).encode("utf-8"))
            self.firt_message = True


        message = str(self.client.recv(8096).decode("utf-8"))
        if message is None or message == "[EXIT]":
            self.client.close()
            return

        print("[+] client send message as: %s" % (message))

        del message

        self.run()

