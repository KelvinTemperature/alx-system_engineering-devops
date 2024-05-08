#!/usr/bin/python3
"""
    Module to print out the first 10 hot
    Posts in a subreddit from Reddit API.
"""
import requests


def top_ten(subreddit):
    """Function to print the first 10 hot posts"""
    u_agent = 'Mozilla/5.0'

    headers = {
            'User-Agent': u_agent
            }

    params = {
            'limit': 10
            }

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    response = requests.get(url,
                            headers=headers,
                            params=params,
                            allow_redirects=False
                            )
    if response.status_code != 200:
        print(None)
        return

    dic = response.json()
    hot_posts = dic['data']['children']
    if len(hot_posts) == 0:
        print(None)
    else:
        for post in hot_posts:
            print(post['data']['title'])
