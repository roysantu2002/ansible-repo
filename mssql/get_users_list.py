
import json
import os
from datetime import datetime

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
datestring = str(int(datetime.now().strftime("%Y%m%d")))
current_path = os.path.join(os.path.dirname(__file__), datestring)

for serverName in server_list:
    # ENCRYPT defaults to yes starting in ODBC Driver 18. It's good to always specify ENCRYPT=yes on the client side to avoid MITM attacks.
    cnxn = mssql_connection(server, database, username, password)
    _user_sql = "select loginname from master.sys.syslogins;"
    user_list = cnxn.get_users(_user_sql)
    user_dict[serverName] = user_list

with open(os.path.join(current_path, _file_name), "w") as write_file:
    json.dump(user_dict, write_file, indent = 4)
