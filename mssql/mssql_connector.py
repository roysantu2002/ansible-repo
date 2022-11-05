import logging as log
import os

import pyodbc


class mssql_connection:
    """mssql db connection"""
    def __init__(self, server, database, username, passw):
        self.server = server
        self.database = database
        self.username = username
        self.passw = passw
        try:
            log.debug("[%s] Opening connection to database", self.server)
            self.connector = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER='+self.server+';DATABASE='+self.database+';ENCRYPT=yes;UID='+self.username+';PWD='+ self.passw +';TrustServerCertificate=yes')
            print("{c} is working".format(c=self.connector))

        except pyodbc.Error as e:
            print(self.server, str(e))
            log.error("[%s] Failed to connect to database: %s", self.server, str(e))
            self.connector.close()

    """
        #TODO:
    """
    def mssql_connector(self) -> str:
        if self.connector:
            return self.connector

    """
        #TODO:
        mssql_ccursor
    """
    def mssql_ccursor(self) -> str:
        if self.connector:
            return self.connector.cursor()

    # def get_users(self) -> dict:


