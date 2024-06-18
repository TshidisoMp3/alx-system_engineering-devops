#!/usr/bin/python3
"""Function that queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """Function that queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit"""
    headers = {'User-agent': 'test'}
    res = requests.get("https://www.reddit.com/r/{}/hot.json?after={}"
                       .format(subreddit, after), headers=headers)
    try:
        for i in res.json()['data']['children']:
            hot_list.append(i['data']['title'])
        after = res.json()['data']['after']
        if after is not None:
            recurse(subreddit, hot_list, after)
        return hot_list
    except Exception:
        return None
