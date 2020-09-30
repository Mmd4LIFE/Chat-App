"""
    created at sep 30/2020 by Mmd4LIFE
    - this package handle socket server tcp
"""
from socket import (
    socket, AF_INET, SOCK_STREAM,
    SOL_SOCKET, SO_REUSEADDR
)


class SocketServer:
    """
        this class for creating stream on  TCP protocol
    """

    def __init__(self):
        super(SocketServer, self).__init__()

        self.sock_connaction = socket(AF_INET, SOCK_STREAM)
        self.sock_connaction.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    def start(self):
        """ this method try creating socket connection
            :params:
            :return:
        """

        self.sock_connaction.bind(())


    
        

