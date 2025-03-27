import requests

url = "http://127.0.0.1:5000/check_fact"
headers = {"Content-Type": "application/json"}
data = {}

response = requests.post(url, json=data, headers=headers)
print(response.status_code)
print(response.json())
