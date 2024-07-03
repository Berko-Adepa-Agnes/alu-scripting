#!/usr/bin/python3
"""
Function that queries the Reddit API and returns
the number of subscribers for a given subreddit.
"""
import requests
import sys


def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers for a given subreddit."""
    u_agent = 'Mozilla/5.0'

    # Set headers with custom User-Agent to avoid rate limiting
    headers = {
        'User-Agent': u_agent
    }

    # Construct the URL to get subreddit info
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    
    try:
        # Make the request to the Reddit API
        res = requests.get(url, headers=headers, allow_redirects=False)
        
        # If the response status is not 200 (OK), return 0
        if res.status_code != 200:
            return 0
        
        # Parse the JSON response
        data = res.json()
        
        # Check if the expected keys are in the response
        if 'data' not in data or 'subscribers' not in data['data']:
            return 0
        
        # Return the number of subscribers
        return data['data']['subscribers']
    
    except requests.RequestException:
        # Handle any request exceptions and return 0
        return 0

# Example usage
if __name__ == "__main__":
    if len(sys.argv) > 1:
        subreddit = sys.argv[1]
        print(f'Number of subscribers in r/{subreddit}: {number_of_subscribers(subreddit)}')
