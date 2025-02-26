from bs4 import BeautifulSoup
import requests

def discover_parameters(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    params = []
    
    forms = soup.find_all('form')
    
    for form in forms:
        action = form.get('action')
        method = form.get('method', 'get').lower()
        inputs = form.find_all('input')
        
        for input_tag in inputs:
            name = input_tag.get('name')
            if name:
                params.append((method, action, name))
                
    links = soup.find_all('a')
    for link in links:
        href = link.get('href')
        if href:
            params.append(('get', href, ''))  # Assume GET for links

    return params

