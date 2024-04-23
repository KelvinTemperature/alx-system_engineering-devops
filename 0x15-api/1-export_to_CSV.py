#!/usr/bin/python3
"""Export Data in the CSV format"""
import csv
import requests
import sys


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'

    user_id = sys.argv[1]

    user_data = requests.get(url + 'users/{}'.format(user_id))
    user_json = user_data.json()
    username = user_json['username']

    todos_data = requests.get(url + 'todos', params={'userId': user_id})
    todos_json = todos_data.json()

    with open('{}.csv'.format(user_id), 'w') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for todo in todos_json:
            writer.writerow([user_id, username, todo['completed'],
                            todo['title']])
