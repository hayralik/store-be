import requests

url = "http://localhost:5000"
header = {"X-Secret-Key": "mysecret"}
#header = {"Alik01": "mysecret"}
response = requests.get(url + "/api/users", headers=header)

print(response)
#print(response.text)    # если хотите сырой ответ
print(response.json())  # вот это напечатает данные
