#!/usr/bin/python3
"""Function that queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit"""

import requests


def top_ten(subreddit):
    """Function that queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit"""
    headers = {'User-agent': 'test'}
    res = requests.get("https://www.reddit.com/r/{}/hot.json?limit=10"
                       .format(subreddit), headers=headers)
    try:
        for i in range(10):
            print(res.json()['data']['children'][i]['data']['title'])
    except Exception:
        print(None)
