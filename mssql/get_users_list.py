
from mssql_connector import mssql_connection

"""
    #TODO:
    transfer to env or config
"""
server = 'localhost'
database = 'master'
username = 'SA'
password = 'Ansible1234'



# ENCRYPT defaults to yes starting in ODBC Driver 18. It's good to always specify ENCRYPT=yes on the client side to avoid MITM attacks.
cnxn = mssql_connection(server, database, username, password)

conn = cnxn.mssql_connector()
cursor = conn.cursor()


#Sample select query
# cursor.execute("SELECT @@version;")
# cursor.execute("select loginname from master.sys.syslogins;")
# row = cursor.fetchone()
# while row:
#     print(row[0])
#     row = cursor.fetchone()

_user_sql = "select loginname from master.sys.syslogins;"
user_list = cnxn.get_users(_user_sql)
print(user_list)