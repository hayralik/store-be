import requests

users = [
    {'id': 1, 'email': 'alik01@mail.com', 'password': 'Alik01'},
    {'id': 2, 'email': 'alik02@mail.com', 'password': 'Alik02'},
    {'id': 3, 'email': 'alik03@mail.com', 'password': 'Alik03'}
    ]
url = "http://localhost:5000"

def post(url, user):
    print(requests.post(url, json=user).json())


for user in users:
    post(url + '/api/register', user)
    
# for user in users:
#    print(requests.post("http://localhost:5000/api/register",
#        json={"email":user['email'],"password":user['password']}).json())
