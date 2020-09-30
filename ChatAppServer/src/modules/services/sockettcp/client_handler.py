"""
    created at sep 30/2020 by Mmd4LIFE
    - this package handle all client that connect
        to our server tcp
"""

from threading import Thread
from datetime import datetime


class ClientHandler:

    def __init__(self, client: object, client_address: object):
        Thread.__init__(self)

        self.client = client
        self.client_address = client_address

    def run(self):
        """ run new client thread from this functin
            :params:
            :return:
        """

        message: str = str(self.client.recv(8096)).decode("utf-8")
        print("[+] client send message as: %s" % (message))

        del message

        self.run()

