#!/usr/bin/python

import json
import os

import requests
import urllib3
from dotenv import load_dotenv

load_dotenv()

tower_base_url = os.environ.get('tower_base_url')
tower_username = os.environ.get('tower_username')
tower_password = os.environ.get('tower_password')


def get_job_events(tower_job_id='1'):

    job_data = {}
    job_data['event_data'] = []

    url = tower_base_url + '/api/v2/jobs/'

    url = tower_base_url + '/api/v2/jobs/' + str(tower_job_id) + '/job_events'

    response = requests.get(url, auth=requests.auth.HTTPBasicAuth(
        tower_username, tower_password), verify=False)

    for result in response.json()['results']:

        if result['summary_fields'] != "":
            if result['event_data']:
                if 'res' in result['event_data']:
                    if 'msg' in result['event_data']['res']:
                        if result['event_data']['res']['msg'] != None:
                            job_data['event_data'].append(
                                result['event_data']['res']['msg'])

    return job_data
