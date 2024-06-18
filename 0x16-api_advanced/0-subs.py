#!/usr/bin/python3
"""Function that queries the Reddit API and returns the number of subscribers"""

import requests


def number_of_subscribers(subreddit):
    """Function that queries the Reddit API and returns the number of subscribers"""
    headears = {'User-Agent': 'Mozilla/5.0'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = requests.get(url, headers=headears)
    if response.status_code == 200:
        return response.json().get('data').get('subscribers')
    return 0
