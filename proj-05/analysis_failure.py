import json
# importing module for regex
import re

import pandas as pd
from pandas import json_normalize

import get_all_failed_jobs as jobs

search_word = ['timed', 'connect']

for i in range(len(search_word)):
    data_found = {}
    with open("sample_job_data.json", "r") as f:
        data = f.read().lower()
        total = data.count(search_word[i])
        data_found[search_word[i]] = total
    print(data_found)
# Reading JSON


# get_data_ = jobs.get_failed_jobs()
# with open("sample_job_data.json", "w") as outfile:
#     json.dump(get_data_, outfile, indent=4)


# Use json_normalize() to convert JSON to DataFrame
with open('sample_job_data.json', encoding="utf8") as f:
    d = json.load(f)
    searchWord = 'Connect'
    total = sum(1 for line in f.readlines() if 'Destination' in line)
    print(total)


# df = pd.read_json('sample_job_data.json')
df1 = pd.DataFrame(d, columns=['id', 'events'])
# df = json_normalize(d, max_level=0)
# _id_count = df['id'].value_counts()
# String to be searched in start of string


def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts


# print(word_count(json.dumps(d)))

# Data Info
# print(df1.info())
# print(df1)
# print(df1.count())
# count the value of single specific columns in dataframe

# print(df1.events.nunique())
# search = "connect"
#
# # count occurrences of the value 'B' in the 'team' column
# count_connect = df.words.str.count("connect")
# # count of occurrence of a and creating new column
# # df["count"] = df['events'].str.count(search, re.I)
#
# # display
# print(count_connect)
