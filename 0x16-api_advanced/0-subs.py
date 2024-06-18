#!/usr/bin/python3
"""Function that queries the Reddit API and returns the number of subscribers"""

import requests


def number_of_subscribers(subreddit):
    """Function that queries the Reddit API and returns the number of subscribers"""
    headears = {'User-Agent': 'Mozilla/5.0'}
    resp = requests.get('https://www.reddit.com/r/{}/about.json'.format(subreddit),
                        headers=headears)
    if resp.status_code == 200:
        return resp.json().get('data').get('subscribers')
    return 0
pass
