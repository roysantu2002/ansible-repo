from mssql_connector import mssql_connection

server = 'localhost'
database = 'master'
username = 'SA'
password = 'Ansible1234'
# ENCRYPT defaults to yes starting in ODBC Driver 18. It's good to always specify ENCRYPT=yes on the client side to avoid MITM attacks.
cnxn = mssql_connection(server, database, username, password)
cursor = cnxn.mssql_ccursor()

#Sample select query
cursor.execute("SELECT @@version;")
row = cursor.fetchone()
while row:
    print(row[0])
    row = cursor.fetchone()