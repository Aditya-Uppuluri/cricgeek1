import requests

def get_live_scores(api_key):
    # Specify the CricAPI endpoint for live scores
    url = 'https://api.cricapi.com/v1/cricScore'
    
    # Specify the parameters required by the API
    params = {
        'apikey': api_key,
        # Add any additional parameters if required by the API
    }
    
    try:
        # Make a GET request to the CricAPI
        response = requests.get(url, params=params)
        data = response.json()
        
        # Check if the request was successful
        if response.status_code == 200:
            return data  # Return the JSON response
            
        # If the request failed, return an error message
        return {'error': 'Failed to fetch live scores'}
    
    except Exception as e:
        # Handle any exceptions that may occur during the request
        return {'error': str(e)}
