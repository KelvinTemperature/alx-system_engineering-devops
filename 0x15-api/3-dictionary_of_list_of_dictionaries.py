#!/usr/bin/python3
"""Fetching all employees data"""
import json
import requests


def get_all_data():
    """fetching all data from the API"""
    url = 'https://jsonplaceholder.typicode.com/'

    users = requests.get(url + 'users').json()

    data = {}

    for user in users:
        user_id = user['id']
        params = {'userId': user_id}

        todos = requests.get(url + 'todos', params=params).json()

        data[user_id] = []

        for todo in todos:
            task_info = {
                    "username": user['username'],
                    "task": todo['title'],
                    "completed": todo['completed'],
                    }
            data[user_id].append(task_info)

    return data


if __name__ == '__main__':
    with open('todo_all_employees.json', 'w') as todo:
        json.dump(get_all_data(), todo)
