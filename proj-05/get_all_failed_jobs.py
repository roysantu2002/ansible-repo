#!/usr/bin/python

"""
    get_failed_jobs
"""
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

tower_base_url = os.environ.get('tower_base_url')
tower_username = os.environ.get('tower_username')
tower_password = os.environ.get('tower_password')
days = os.environ.get('delta_day')


def get_failed_jobs():

    output = []

    url = tower_base_url + '/api/v2/jobs/'
    response = requests.get(url, auth=requests.auth.HTTPBasicAuth(
        tower_username, tower_password), verify=False)
#
    for result in response.json()['results']:
        job_data = {}
        created_dt = result['created']
        end_date = date.today() + timedelta(days=int(days))
        end_date_int = int(end_date.strftime("%Y%m%d%H%M%S"))
        start_date = datetime.strptime(
            created_dt, '%Y-%m-%dT%H:%M:%S.%fZ')
        start_date_int = int(start_date.strftime("%Y%m%d%H%M%S"))

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

                output.append(job_data)
    return output
