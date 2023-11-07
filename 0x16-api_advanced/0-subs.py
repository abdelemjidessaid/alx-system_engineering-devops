#!/usr/bin/python3
"""
    Script that request the number of subscribers of a user from reddit
"""
import requests


def number_of_subscribers(subreddit):
    """
        function that returns the number of subscribers
    """
    url = " https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    response = requests.get(url=url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0

    data_json = response.json()
    data = data_json.get('data')

    return data.get('subscribers')
