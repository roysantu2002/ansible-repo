
import json

import yaml
from common_func import common_func as util
from mssql_connector import mssql_connection

"""
    #TODO:
    transfer to env or config
"""
server = 'localhost'
database = 'master'
username = 'SA'
password = 'Ansible1234'

"""
    userid

"""

server_list = ['www.server1.com', 'www.server2.com', 'www.server3.com', 'www.server4.com']
user_dict = dict()
_file_name = util().create_file()
print(_file_name)
for serverName in server_list:
    # ENCRYPT defaults to yes starting in ODBC Driver 18. It's good to always specify ENCRYPT=yes on the client side to avoid MITM attacks.
    cnxn = mssql_connection(server, database, username, password)
    # conn = cnxn.mssql_connector()
    # cursor = conn.cursor()


    #Sample select query
    # cursor.execute("SELECT @@version;")
    # cursor.execute("select loginname from master.sys.syslogins;")
    # row = cursor.fetchone()
    # while row:
    #     print(row[0])
    #     row = cursor.fetchone()


    _user_sql = "select loginname from master.sys.syslogins;"
    user_list = cnxn.get_users(_user_sql)
    user_dict[serverName] = user_list


with open(_file_name, "w") as write_file:
    json.dump(user_dict, write_file, indent = 4)

    # Serializing json
    # json_object = json.dumps(user_dict, indent = 4)
    # print(json_object)

    # print(json_object)

    # with open("user_data.yaml", 'r') as file:
    #     try:
    #          documents = yaml.safe_dump(user_dict, file, sort_keys=False)
    #     #    documents = yaml.safe_dump(user_dict, file, sort_keys=False, default_flow_style=False, indent=None)
    #     except yaml.YAMLError as exc:
    #         print(exc)
