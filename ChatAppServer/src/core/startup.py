"""
    created at sep 30/2020 by Mmd4LIFE
    - start app from this class
"""

class StartUp:

    def __init__(self):
        super(StartUp, self).__init__()

    def __start_sockettcp_service__(self):
        """ this function start socket tcp service
            :params:
            :return:
        """
        from modules.services.sockettcp.socket_server import SocketServer

        SocketServer().run()

    def __start_db_service__(self):
        # from ChatAppServer.src.modules.data.app_context import AppContext
        from modules.data.app_context import AppContext
        # from ChatAppServer.src.modules.models.user import User
        from modules.models.user import User

        app_context = AppContext()
        app_context.inject_db_set(User().get_types)
        app_context.start()

    def start(self):
        """ this function start app from this lines
            :params:
            :return:
        """

        self.__start_db_service__()

        self.__start_sockettcp_service__()

