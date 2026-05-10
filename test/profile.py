import requests
from base_url import base_url

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc3ODM4MjY2NiwianRpIjoiODc4Mzg0ODItZWViZS00MGVjLTk2OWEtMjg5NjE2ZWU1YjE3IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjEiLCJuYmYiOjE3NzgzODI2NjYsImNzcmYiOiJiMjk0NmE0Ny0xZDQ4LTQ5NDItODdjZC1iZDFjMWY4MTU4Y2MiLCJleHAiOjE3Nzg0NjkwNjZ9.z3CNwF3kAmDw1xOsj-lwWfy34QB1t2Y8-LIKKaYcdUI"

headers = {"Authorization": f"Bearer {token}"}
response = requests.get(base_url + "/api/profile", headers=headers)
print(response.json())
