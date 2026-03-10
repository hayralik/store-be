import requests

url = "http://localhost:5000"
endpoint = "/api/login"
# headers = {"Content-Type": "application/json"}
user = {'id': 1, 'email': 'alik01@mail.com', 'password': 'Alik01'}
data = {'email': user['email'], 'password': user['password']}

#response = requests.post(url + endpoint, headers=headers, json=data)
response = requests.post(url + endpoint, json=data)
print(response.json())  # вот это напечатает данные

