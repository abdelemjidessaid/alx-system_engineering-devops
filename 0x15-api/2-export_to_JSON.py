#!/usr/bin/python3
"""
    Python script to export data in the JSON format.
"""

import json
import requests
from sys import argv


if __name__ == '__main__':
    # initialize variables:
    user_id = argv[1]
    tasks = []
    formated_tasks = {}
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
    # save all tasks as object:
    for task in todos_json:
        tasks.append({
            'task': task.get('title'),
            'completed': task.get('completed'),
            'username': user_json.get('username')
        })
    # format the object of tasks as JSON file:
    formated_tasks[user_id] = tasks
    json_file = user_id + '.json'
    # save all tasks to this JSON file:
    with open(json_file, 'w') as file:
        json.dump(formated_tasks, file)
