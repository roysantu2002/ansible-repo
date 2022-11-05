# import the mysql client for Python

import csv
import sys

import pandas as pd
import pymssql

""" Connect to the MySQL Database Server """


dbIPAddresss = "localhost"

dbUsr = "SA"

dbPwd = "ansible1234"

dbName = "master"

# dbCharset       = "utf8mb4"
#
# cursorType      = pymysql.cursors.DictCursor


try:

    mySQLConnection = pymssql.connect(dbIPAddresss, dbUsr, dbPwd, dbName)
#
#
#     mySQLConnection   = pymysql.connect(host=dbIPAddresss,
#
#                                     user=dbUsr,
#
#                                     password=dbPwd,
#
#                                     db=dbName,
#
#                                     charset=dbCharset,
#
#                                     cursorclass=cursorType,
#
#                                     autocommit=True)

    """ Get a cursor object from the connection """

    cursorObject = mySQLConnection.cursor()

    getDBList = "SHOW DATABASES"

    getUserSQL = "select user from user group by user"

    # Execute the SQL query for retrieving the user list from MySQL

    cursorObject.execute(getDBList)

   # Fetch all the user records

    sqlDBList = cursorObject.fetchall()

    # Print the MySQL user name

    for user in sqlDBList:

        print(user)

    # Execute the SQL SELECT query

    cursorObject.execute(getUserSQL)

    # Fetch all the user records

    sqlUsers = cursorObject.fetchall()

    df = pd.DataFrame(sqlUsers)
    # place 'r' before the path name
    df.to_csv('exported_data_01.csv', index=False)

    m_dict = list(sqlUsers)


except Exception as e:

    print("Exeception occured:{}".format(e))


finally:

    mySQLConnection.close()
