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

#from ChatAppServer.src.modules.data.app_context import AppContext
from modules.data.app_context import AppContext

class MassageHandler:

    def __init__(self, socket_client: socket):
        super(MassageHandler, self).__init__()
        self.app_context = AppContext()

        self.socket_client = socket_client

    def start(self):
        message: str = self.socket_client.recv(8096).decode("utf-8")
        data_json = json_loads(message)
        
        if data_json["command"] == "AUTH":
            username: str = data_json["message"]["username"]
            password: str = data_json["message"]["password"]

            if self.app_context.is_exist_in_db("user", "username", username):
                if self.check_auth(
                    username,
                    password
                ):
                    print("User authenticated successfully")
                else:
                    print("password is not valid")
            else:
                self.app_context.insert_query(
                    command=f"""
                        insert into user (username, password) values ('{username}', '{password}');
                    """
                )

        #    del username, password

        #if message is None or message == "[EXIT]":
        #    self.socket_client.close()
        #    return

        #print("[+] client send message as: %s" % (message))

        del message

        self.start()

    def check_auth(self, username: str, password: str):
        """ check authentication of user
        :param username:
        :param password:
        :return:
        """

        result = self.app_context.select_query(
            command=f"""
                select id from user where username=='{username}' and password=='{password}'
            """
        )

        is_exist = None
        for row in result:
            if row is not None:
                is_exist = True

        return is_exist

