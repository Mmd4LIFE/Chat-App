"""
    created at oct 02/2020 by Mmd4LIFE
    - app context for connecting to database
"""

from sqlite3 import connect
from typing import Set

#from ChatAppServer.src.commons.constants.paths import DATABASE_PATH
from commons.constants.paths import DATABASE_PATH
#from ChatAppServer.src.modules.models.user import *
from modules.models import *


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

            feilds_and_type = data_list[1:]
            feilsd_string: str = ""
            for feilsds in feilds_and_type:
                feilsds_name: str = feilsds[0]
                feilsds_type: str = feilsds[1]

                feilsd_string += feilsds_name + " " + feilsds_type + ","
                # """ username nvarchar(100), password nvarchar(100), """

            feilsd_string = feilsd_string[:len(feilsd_string): - 1]

            #command = f"""
            #    create table if not exists {data_list[0][0]}(

            #        {feilsd_string}
            #    );
            #"""
            #command = f"""
            #    CREATE TABLE if not exists {data_list[0][0]}
            #        id integer PRIMARY KEY AUTOINCREMENT,
            #        {feilsd_string}
            #    ;
            #"""

            #cur.execute(command)

            cur.execute(f"""
                CREATE TABLE if not exists {data_list[0][0]}(
                    id integer PRIMARY KEY AUTOINCREMENT,
                    {feilsd_string}
                );
            """)

        self.connection.commit()

    def start(self):
        self.__create_tables__()





