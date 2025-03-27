import json
import requests

# Your API Key (replace with the actual key)
API_KEY = "AIzaSyB5gIWYw6SnYIWggL2J4dkTU7wGi7m3Euk"

def fact_check(query):
    """
    Fetch fact-checking results for a given query.
    """
    api_url = f"https://factchecktools.googleapis.com/v1alpha1/claims:search?query={query}&key={API_KEY}"
    
    response = requests.get(api_url)
    
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Failed to fetch data. Status code: {response.status_code}"}

# Example Usage:
query = "Covid-19 vaccines cause infertility"
result = fact_check(query)
print(json.dumps(result, indent=2))
