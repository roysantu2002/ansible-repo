import json

import pandas as pd
from pandas import json_normalize

import get_all_failed_jobs as jobs

# Reading JSON


get_data_ = jobs.main()
with open("sample_job_data.json", "w") as outfile:
    json.dump(get_data_, outfile, indent=4)


# Use json_normalize() to convert JSON to DataFrame
with open('sample_job_data.json') as f:
    d = json.load(f)
# df = pd.read_json('sample_job_data.json')
df = json_normalize(d)

print(df)
