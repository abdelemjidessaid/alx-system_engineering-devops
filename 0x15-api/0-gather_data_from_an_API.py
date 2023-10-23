#!/usr/bin/python3
"""
    Script that using this REST API, for a given employee ID,
    returns information about his/her TODO list progress.
"""

import requests
from sys import argv


if __name__ == '__main__':
    # initialize variables:
    user_id = argv[1]
    tasks = 0
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
    # loop over the todos data to count the tasks completed:
    for task in todos_json:
        if task['completed']:
            tasks += 1
    # print the important data:
    print(
        'Employee {} is done with tasks({}/{}):'
        .format(user_json['name'], tasks, len(todos_json))
    )
    # print the compeleted tasks:
    for task in todos_json:
        if task['completed']:
            print(
                '\t ' + task.get('title')
            )
