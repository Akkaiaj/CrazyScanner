import requests
import random
import time

def send_request(url, method="GET", params=None, data=None):
    try:
        user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Safari/605.1.15',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0'
        ]

        headers = {'User-Agent': random.choice(user_agents)}

        print(f"[DEBUG] Sending {method} request to: {url} with params: {params}, headers: {headers}")

        if method == "GET":
            response = requests.get(url, params=params, headers=headers)
        elif method == "POST":
            response = requests.post(url, data=data, headers=headers)
        
        print(f"[DEBUG] Received status code: {response.status_code}")
        
        time.sleep(random.uniform(0.5, 2.0))  # Random sleep between 0.5 and 2 seconds
        
        return response.text, response.status_code, response.headers # Added the headers
        
    except requests.RequestException as e:
        print(f"Request Exception: {e}")
        return None, None , None # And add a header here

