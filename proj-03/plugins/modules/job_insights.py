#!/usr/bin/python

ANSIBLE_METADATA = {'metadata_version': '1.1',
                   'status': ['preview'],
                  'supported_by': 'none'}

import json

import requests
import urllib3
from ansible.module_utils.basic import AnsibleModule
from requests.auth import HTTPBasicAuth

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def main():

    module = AnsibleModule(
     supports_check_mode = True,
     argument_spec = dict(
          tower_base_url = dict(type='str', required=True),
          tower_username = dict(type='str', required=True),
          tower_password = dict(type='str', required=True, no_log=True),
          tower_job_id = dict(type='str', required=True),
          tower_auth_token = dict(type='str', required=True),
       ),
    )
    output = dict(value='',)
    job_data = {}
    job_data['summary_fields']=[]
    job_data['event_data']=[]

    tower_base_url = module.params['tower_base_url']
    tower_username = module.params['tower_username']
    tower_password = module.params['tower_password']
    tower_job_id = module.params['tower_job_id']
    tower_auth_token = module.params['tower_auth_token']
    headers = {
        'Authorization': 'Bearer ' + tower_auth_token,
        'Content-Type': 'application/json'
    }


    url = tower_base_url + '/api/v2/jobs/' + tower_job_id + '/job_events'
    # url = tower_base_url + '/api/v2/jobs/' + tower_job_id + '/stdout/'
    # worflow_job_node = response.json()['results'][0]['id']
    response = requests.get(url, auth=requests.auth.HTTPBasicAuth(tower_username, tower_password), verify=False)

    for result in response.json()['results']:

        if result['summary_fields']!= "":
            job_data['summary_fields'].append(result['summary_fields'])

            # event_data['summary_fields']=result['summary_fields']
            if result['event_data']:
                if "res" in result['event_data']:
                    job_data['event_data'] = result['event_data']
                # print(result['event_data'])
                # event_data.append(result['res'])
                # output.append(result['event_data'])
                    # output.setdefault(result['summary_fields'],[]).append(result['event_data'])
        # if response.json()['next'] == None:
        #     break

    # print(response)
    # # output['job_id'] = response.json()['results'][0]['summary_fields']['job']['id']
    # results = response.json()['results']
    # output['summary_fields'] = response.json()['results'][len(results) - 1]['summary_fields']
    # output['event_data'] = response.json()['results'][len(results) - 1]['event_data']
    output['value'] = job_data

    module.exit_json(**output)

if __name__ == '__main__':
    main()
