import hashlib
import logging as log
import os
import sys

import pyodbc

log.basicConfig(
    level=log.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        log.FileHandler("debug.log"),
        log.StreamHandler(sys.stdout)
    ]
)
class mssql_connection:

    """mssql db connection"""
    def __init__(self, server, database, username, passw):
        self.server = server
        self.database = database
        self.username = username
        self.passw = passw
        try:
            log.debug("[%s] Opening connection to database", self.server)
            log.info("[%s] connecting ...", self.server)
            self.connector = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER='+self.server+';DATABASE='+self.database+';ENCRYPT=yes;UID='+self.username+';PWD='+ self.passw +';TrustServerCertificate=yes')
            log.info("[%s] connected", self.server)

        except pyodbc.Error as e:
            log.error("[%s] Failed to connect to database: %s", self.server, str(e))
            self.connector.close()

    """
        #TODO:
    """
    def mssql_connector(self) -> str:
        if self.connector:
            return self.connector
        else:
            return None

    """
        #TODO:
        mssql_ccursor
    """
    def cursor(self):
        if self.connector:
            return self.connector.cursor()
        else:
            return None

    """
        #TODO:
        mssql_ccursor
    """
    def get_users(self, sql: str) -> list:
        cursor = self.cursor()
        cursor.execute(sql)
        users_list = []
        users_ = [item[0] for item in cursor.fetchall()]
        # users_ = cursor.fetchall()
        if len(users_)==0:
            return None
        else:
            for user in users_:
                user_id_sha256 = hashlib.sha256(user.encode())
                users_list.append(user_id_sha256.hexdigest())
            return users_list



