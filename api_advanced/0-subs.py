#!/usr/bin/python3
"""
Function that queries the Reddit API and returns
the number of subscribers for a given subreddit.
"""

import requests
import sys

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        int: The number of subscribers if the subreddit is valid, otherwise 0.
    """
    # Set the User-Agent to avoid 'Too Many Requests' errors from Reddit
    u_agent = 'Mozilla/5.0'

    # Set headers with the custom User-Agent
    headers = {
        'User-Agent': u_agent
    }

    # Construct the URL to get subreddit info
    url = "https://api.reddit.com/r/{}/about.json".format(subreddit)
    
    try:
        # Make the request to the Reddit API
        res = requests.get(url, headers=headers, allow_redirects=False)
        
        # If the response status code is not 200, return 0
        if res.status_code != 200:
            return 0
        
        # Parse the JSON response
        data = res.json()
        
        # Check if the 'data' and 'subscribers' keys are in the response
        if 'data' not in data or 'subscribers' not in data['data']:
            return 0
        
        # Return the number of subscribers
        return data['data']['subscribers']
    
    except requests.RequestException:
        # Handle any request exceptions and return 0
        return 0
    