import pandas as pd
import pyodbc
import yaml

# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
# server = 'tcp:myserver.database.windows.net'
server = 'localhost'
database = 'master'
username = 'SA'
password = 'Ansible1234'
# ENCRYPT defaults to yes starting in ODBC Driver 18. It's good to always specify ENCRYPT=yes on the client side to avoid MITM attacks.
cnxn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER='+server+';DATABASE='+database+';ENCRYPT=yes;UID='+username+';PWD='+ password+';TrustServerCertificate=yes')
cursor = cnxn.cursor()

#Sample select query
cursor.execute("SELECT @@version;")
row = cursor.fetchone()
while row:
    print(row[0])
    row = cursor.fetchone()

# Initialise the Cursor
# cursor = connection.cursor()
# Executing a SQL Query
cursor.execute('select loginname from master.sys.syslogins')

sqlUsers = cursor.fetchall()

df = pd.DataFrame(sqlUsers['loginname'])

# place 'r' before the path name
df.to_csv('exported_data_01.csv', index=False)

with open('test_df_to_yaml.yaml', 'w') as file:
    documents = yaml.dump({server: df.to_dict(orient='records')}, file, default_flow_style=True)


# with open('test_df_to_yaml.yaml', mode="rt", encoding="utf-8") as test_df_to_yaml:
#     df_merged = pd.DataFrame(yaml.full_load(test_df_to_yaml)['result'])

