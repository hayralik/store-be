import requests
from base_url import base_url

header = {"X-Secret-Key": "mysecret"}
#header = {"Alik01": "mysecret"}
response = requests.get(base_url + "/api/users", headers=header)

#print(response)
#print(response.text)    # если хотите сырой ответ
print(response.json())  # вот это напечатает данные

#print(response.status_code)
#print(response.text)