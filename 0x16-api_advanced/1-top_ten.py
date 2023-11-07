#!/usr/bin/python3
"""
    that queries the Reddit API and prints the titles
    of the first 10 hot posts listed for a given subreddit
"""
import requests


def top_ten(subreddit):
    """
        function that queries the Reddit API
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    response = requests.get(
        url=url, headers=headers,
        allow_redirects=False, params={"limit": 10}
    )
    if response.status_code == 404:
        print("None")
        return
    data_json = response.json().get('data').get('children')
    for i in data_json:
        print(i.get('data').get('title'))
