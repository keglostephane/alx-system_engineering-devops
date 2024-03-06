#!/usr/bin/python3
"""reddit_subscribers

fetch the number of subscribers for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """return the number of subscribers for a given subreddit.

    :param subredit: subreddit name
    :type subredit: str
    :return: the number of subscribers for the subreddit
    :rtype: int
    """
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'Firefox/5.0'}
    req = requests.get(url, headers=headers, allow_redirects=False)

    if req.status_code == 200:
        result = req.json()
        return result.get("data").get("subscribers")
    else:
        return 0
