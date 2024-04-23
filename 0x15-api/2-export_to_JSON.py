#!/usr/bin/python3
"""Export data in JSON format"""
import json
import requests
import sys


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'

    user_id = sys.argv[1]

    user = requests.get(url + 'users/{}'.format(user_id)).json()
    todos = requests.get(url + 'todos', params={'userId': user_id}).json()

    data = {user_id: []}
    for todo in todos:
        task_info = {
                "task": todo['title'],
                "completed": todo['completed'],
                "username": user['name']
                }
        data[user_id].append(task_info)

    with open('{}.json'.format(user_id), 'w') as file:
        json.dump(data, file)
