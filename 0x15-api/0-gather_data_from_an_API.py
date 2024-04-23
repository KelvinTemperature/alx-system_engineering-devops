#!/usr/bin/python3
"""Returns information on the TODO list of an Employee"""
import requests
import sys


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'

    emp_id = sys.argv[1]

    user_data = requests.get(url + 'users/{}'.format(emp_id))
    user_json = user_data.json()

    todos_data = requests.get(url + 'todos', params={'userId': emp_id})
    todos_json = todos_data.json()

    completed = []
    for todo in todos_json:
        if todo['completed'] is True:
            completed.append(todo['title'])

    print('Employee {} is done with tasks({}/{}):'
          .format(user_json['name'], len(completed), len(todos_json)))

    for title in completed:
        print('\t {}'.format(title))
