#!/usr/bin/python3
"""
   Function that queries a Reddit API an returns
   number iof subscribers.
"""
import requests
import sys


def number_of_subscribers(subreddit):
    """Funtion to return the number of subscribers"""
    u_agent = 'Mozilla/5.0'

    header = {
            'User-Agent': u_agent
            }

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, header, allow_redirects=False)
    if response.status_code != 200:
        return 0
    dic = response.json()
    if "data" not in dic:
        return 0
    if "subscribers" not in dic.get('data'):
        return 0
    return dic['data']['subscribers']
