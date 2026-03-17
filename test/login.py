import requests
from base_url import base_url

endpoint = "/api/login"
# headers = {"Content-Type": "application/json"}
user = {'id': 1, 'email': 'alik01@mail.com', 'password': 'Alik01'}
data = {'email': user['email'], 'password': user['password']}

#response = requests.post(url + endpoint, headers=headers, json=data)
response = requests.post(base_url + endpoint, json=data)


print(response.status_code)
print(response.text)
#print(response.json())  # вот это напечатает данные

