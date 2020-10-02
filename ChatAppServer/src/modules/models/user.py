"""
    created at oct 02/2020 by Mmd4LIFE
    - user model in database
"""

class User:

    def __init__(self):
        super(User, self).__init__()

        self._username: str = None
        self._password: str = None

    @property
    def username(self):
        # get username from local variable
        return self._username

    @username.setter
    def username(self, username):
        # set username to local variable
        self._username = username

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password

    @property
    def get_types(self):
        return [
            ["user", "table"],
            ["username", "nvarchar(100)"],
            ["password", "nvarchar(100)"]
        ]