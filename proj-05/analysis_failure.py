import json

import get_all_failed_jobs as jobs

get_data_ = jobs.main()
with open("sample_job_data.json", "w") as outfile:
    json.dump(get_data_, outfile, indent=4)
