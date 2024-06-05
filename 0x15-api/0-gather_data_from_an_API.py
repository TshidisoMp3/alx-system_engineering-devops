#!/usr/bin/python3
"""Gather data from an API"""

import requests
from sys import argv


if __name__ == "__main__":
    user_id = argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    response = requests.get(url)
    user = response.json()
    name = user.get('name')

    url = 'https://jsonplaceholder.typicode.com/todos'
    response = requests.get(url)
    todos = response.json()
    total_tasks = len(todos)
    done_tasks = [task for task in todos if task.get('completed') is True]

    print('Employee {} is done with tasks({}/{}):'.format(name,
                                                          len(done_tasks),
                                                          total_tasks))
    for task in done_tasks:
        print('\t {}'.format(task.get('title')))
