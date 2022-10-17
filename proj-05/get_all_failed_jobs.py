#!/usr/bin/python

import datetime
import json
import os
from datetime import date, datetime, timedelta

import requests
import urllib3
from dotenv import load_dotenv

import date_util as setdate
import get_job_events_details

load_dotenv()

print(os.environ.get('tower_auth_token'))

tower_base_url = os.environ.get('tower_base_url')
tower_username = os.environ.get('tower_username')
tower_password = os.environ.get('tower_password')
# tower_job_id : 20
# tower_auth_token: AqiyDZJy0qnHY2TlfbJn467FJmP2n1
#
#
# ANSIBLE_METADATA = {'metadata_version': '1.1',
#                    'status': ['preview'],
#                   'supported_by': 'none'}
#


# from ansible.module_utils.basic import AnsibleModule
# from requests.auth import HTTPBasicAuth
#
# urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
#
def main():
    #
    #     module = AnsibleModule(
    #      supports_check_mode = True,
    #      argument_spec = dict(
    #           tower_base_url = dict(type='str', required=True),
    #           tower_username = dict(type='str', required=True),
    #           tower_password = dict(type='str', required=True, no_log=True),
    #           tower_job_id = dict(type='str', required=True),
    #           tower_auth_token = dict(type='str', required=True),
    #        ),
    #     )
    output = []

    # job_data['url'] = []
    # job_data['status'] = []
    # job_data['job_template'] = []
    # job_data['inventory'] = []
    # job_data['project'] = []
    # job_data['events'] = []
#
#     tower_base_url = module.params['tower_base_url']
#     tower_username = module.params['tower_username']
#     tower_password = module.params['tower_password']
#     tower_job_id = module.params['tower_job_id']
#     tower_auth_token = module.params['tower_auth_token']
#     headers = {
#         'Authorization': 'Bearer ' + tower_auth_token,
#         'Content-Type': 'application/json'
#     }
#
#
    url = tower_base_url + '/api/v2/jobs/'
    # url = tower_base_url + '/api/v2/jobs/' + tower_job_id + '/stdout/'
#     # worflow_job_node = response.json()['results'][0]['id']

    response = requests.get(url, auth=requests.auth.HTTPBasicAuth(
        tower_username, tower_password), verify=False)
#
    for result in response.json()['results']:
        job_data = {}
        # int(current_date.strftime("%Y%m%d%H%M%S")
        created_dt = result['created']

        end_date = date.today() + timedelta(days=0)
        end_date_int = int(end_date.strftime("%Y%m%d%H%M%S"))
        # print(int(start_date.strftime("%Y%m%d%H%M%S")))
        start_date = datetime.strptime(
            created_dt, '%Y-%m-%dT%H:%M:%S.%fZ')

        start_date_int = int(start_date.strftime("%Y%m%d%H%M%S"))
#

        # print(setdate.date_range(start_date, end_date))

        # date_time_obj = datetime.strptime(created_dt, '%d/%m/%y %H:%M:%S')
        # today_dt = datetime.datetime(date.today())
        # print(date_time_obj)
        if(start_date_int >= end_date_int):
            if result['failed']:
                _events_details = str(result['id']) + '_events'
                _events_details = get_job_events_details.get_job_events(
                    (result['id']))

                job_data['id'] = result['id']
                job_data['name'] = result['name']
                job_data['url'] = result['url']
                job_data['status'] = result['status']
                job_data['job_template'] = result['job_template']
                job_data['inventory'] = result['inventory']
                job_data['created_by'] = result['summary_fields']['created_by']
                job_data['credentials'] = result['summary_fields']['credentials']
                job_data['events'] = _events_details
                # job_data['status'].append(result['status'])
                # job_data['job_template'].append(result['job_template'])
                # job_data['project'].append(result['project'])
                # job_data['events'].append(_events_details)
                output.append(job_data)
    return output


#
if __name__ == '__main__':
    main()
