"""
    created at oct 01/2020 by Mmd4LIFE
    - this package act as client socket service for
        connection to server
"""

from socket import (
    socket, AF_INET, SOCK_STREAM,
    SOL_SOCKET, SO_REUSEADDR
)
from utils.config_manager import ConfigManager
from commons.constants.colors import Colors

class SocketClientTCP:

    def __init__(self):
        super(SocketClientTCP, self).__init__()

        self.config_manager = ConfigManager()

        self.sock = socket(AF_INET, SOCK_STREAM)
        self.sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

        self.__connect__()

    def __connect__(self):
        """ this function try connection to server
        :param:
        :return:
        """
        print(
            Colors.FORE_YELLOW + "[+] try connection to ChatApp server ..."
              )
        response_code = self.sock.connect_ex((
            self.config_manager.get().socket_server.IP,
            self.config_manager.get().socket_server.PORT,
        ))

        if response_code == 0:
            print(
                Colors.FORE_GREEN + "[+] connecting to ChatApp server was successfully ..."
            )
            ack_know = self.sock.recv(8096)
            if ack_know is None:
                pass
            print(ack_know)
            self.sock.sendall("[EXIT]".encode("utf-8"))

        elif response_code == 111:
            print(
                Colors.FORE_GREEN + "[-] ChatApp server not respod, maybe it is down..."
            )







