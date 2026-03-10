import requests

url = "http://localhost:5000"

response = requests.get(url + "/api/users")
print(response.json())