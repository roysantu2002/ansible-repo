import hashlib
import logging as log
import os
import sys

import pyodbc
from ea_rsa_encrypt import ea_encrypt_ad_login as ea_encrypt

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


    """
        #TODO:
    """
    def mssql_connector(self) -> str:
        try:
            log.debug("[%s] Verify the connection ...", self.server)
            log.info("[%s] connecting ...", self.server)
            if self.connector:
                return self.connector
            else:
                return None
        except pyodbc.Error as e:
            log.error("[%s] Failed to connect to database: %s", self.server, str(e))

    """
        #TODO:
        mssql_ccursor
    """
    def cursor(self):
         try:
            log.debug("[%s] Verify the connection ...", self.server)
            log.info("[%s] connecting ...", self.server)
            if self.connector:
                return self.connector.cursor()
            else:
                return None
         except pyodbc.Error as e:
            log.error("[%s] Failed to connect to database: %s", self.server, str(e))

    """
        #TODO:
        mssql_ccursor
    """
    def get_users(self, sql: str) -> list:

        try:
            log.debug("[%s] Verify the connection ...", self.server)
            log.info("[%s] connecting ...", self.server)
            #
            #         """
            #             ea_encrypt
            #         """
            #         (publicKey, privateKey) = ea_encrypt.loadKeys()


            cursor = self.cursor()
            if cursor is not None:
                cursor.execute(sql)

                users_list = []
                users_ = [item[0] for item in cursor.fetchall()]
                # users_ = cursor.fetchall()
                if len(users_)==0:
                    return None
                else:
                    for user in users_:
                        # encrypt_user = ea_encrypt.encrypt_message(str(user), publicKey)
                        # print(encrypt_user)
                        user_id_sha256 = hashlib.sha256(user.encode())
                        # users_list = (user_id_sha256.hexdigest())
                        users_list.append(user_id_sha256.hexdigest())

                    self.connector.close()
                    return users_list
            else:
                return []
        except pyodbc.Error as e:
            log.error("[%s] Failed to connect to database: %s", self.server, str(e))



