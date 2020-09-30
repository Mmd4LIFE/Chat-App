"""
    created at sep 30/2020 by Mmd4LIFE
    - this package handle socket server tcp
"""
from socket import (
    socket, AF_INET, SOCK_STREAM,
    SOL_SOCKET, SO_REUSEADDR
)
from datetime import datetime

from utils.config_manager import ConfigManager
from commons.constants.colors import Color

from .client_handler import ClientHandler

class SocketServer:
    """
        this class for creating stream on  TCP protocol
    """

    def __init__(self):
        super(SocketServer, self).__init__()

        self.config_manager = ConfigManager()

        self.sock_connaction = socket(AF_INET, SOCK_STREAM)
        self.sock_connaction.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

        self.__start__()

    def __start__(self):
        """ this method try creating socket connection
            :params:
            :return:
        """

        self.sock_connaction.bind((
            self.config_manager.get().socket_server.IP,
            self.config_manager.get().socket_server.PORT
        ))

        self.sock_connaction.listen(
            self.config_manager.get().socket_server.LISTEN_CLIENT
        )

        print(Color.YELLOW + str(datetime.now()).split('.')[0] +
        " => [+] Server ready to listening" + 
        Color.WHITE)

    def run(self):
        """ start server for listining clients
            :params:
            :return:
        """

        client, client_address = self.sock_connaction.accept()

        # we create new thread per client thet connect to server
        ClientHandler(
            client= client,
            client_address= client_address
        ).start()

        self.run()

    
        

