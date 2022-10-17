#!/usr/bin/env python

import json


def _inventory_data():
    return {
        "database": {
            "hosts":
             ["_db"],
            "vars": {
                "ansible_ssh_pwd": "1235",
                "ansible_ssh_usr": "usr"
            }

        }
    }
if __name__ == "__main__":
    invenory_data = _inventory_data()
    print(json.dumps(invenory_data))
