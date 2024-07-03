import requests

def number_of_subscribers(subreddit):
    # Setting the User-Agent to avoid 'Too Many Requests' errors
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    # URL to get subreddit info
    url = f'https://api.reddit.com/r/{subreddit}/about.json'
    
    try:
        # Make the request to the Reddit API
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            # Return the number of subscribers
            return data['data']['subscribers']
        else:
            # If subreddit is invalid or request failed
            return 0
    except requests.RequestException:
        # Handle any request exceptions
        return 0
    