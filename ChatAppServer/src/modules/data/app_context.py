"""
    created at oct 02/2020 by Mmd4LIFE
    - app context for connecting to database
"""

from sqlite3 import connect
from typing import List

#from ChatAppServer.src.commons.constants.paths import DATABASE_PATH
from commons.constants.paths import DATABASE_PATH
#from ChatAppServer.src.modules.models.user import *
from modules.models import *
#from ChatAppServer.src.modules.models.user import User


class AppContext:

    def __init__(self):
        self.tables: List = list()

        self.connection = connect(DATABASE_PATH)


    def inject_db_set(self, dbset: list):
        self.tables.append(dbset)


    def __create_tables__(self):
        cur = self.connection.cursor()

        for item in self.tables:

            data_list = item
            feilds_and_types = data_list[1:]
            feild_string: str = ""
            
            for feilds in feilds_and_types:

                feilds_name: str = feilds[0]
                feilds_type: str = feilds[1]

                feild_string += feilds_name + " " + feilds_type + ","

            feild_string = feild_string[:len(feild_string) - 1]

            command = f"""
                CREATE TABLE if not exists user(
                    id integer PRIMARY KEY AUTOINCREMENT,
                    {feild_string}
                );
            """
            cur.execute(command)

        self.connection.commit()

    def start(self):
        self.__create_tables__()





