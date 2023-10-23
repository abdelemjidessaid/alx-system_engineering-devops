#!/usr/bin/python3
"""
Python script to export data in the CSV format.
"""

import csv
import requests
from sys import argv


if __name__ == '__main__':
    # initialize variables:
    user_id = argv[1]
    username = ''
    session = requests.Session()
    # build the specified urls:
    todos = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(
        user_id
    )
    user = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    # get the data:
    todos_data = session.get(todos)
    user_data = session.get(user)
    # convert the retrieved data to JSON:
    todos_json = todos_data.json()
    user_json = user_data.json()
    username = user_json.get('name')
    # export data as CSV file:
    with open('{}.csv'.format(str(user_id)), 'w', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',', quoting=csv.QUOTE_ALL)
        for task in todos_json:
            writer.writerow(
                [str(user_id), username, task.get('completed'),
                 task.get('title')]
            )
