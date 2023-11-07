#!/usr/bin/python3
"""
    Script that retrieve all posts of a user from Reddit
"""
import requests
after = None


def recurse(subreddit, hot_list=[]):
    """
        recursive function that queries the Reddit API and returns
        a list containing the titles of all hot articles
        for a given subreddit
    """
    global after
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    agent = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    para = {
        'after': after
    }
    results = requests.get(
        url, params=para, headers=agent, allow_redirects=False
    )

    if results.status_code == 200:
        after_data = results.json().get("data").get("after")
        if after_data is not None:
            after = after_data
            recurse(subreddit, hot_list)
        all_titles = results.json().get("data").get("children")
        for title_ in all_titles:
            hot_list.append(title_.get("data").get("title"))
        return hot_list
    else:
        return (None)
