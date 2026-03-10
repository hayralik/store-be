import requests

url = "http://localhost:5000"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc3MzEyNDE5MiwianRpIjoiOGQ3ODRkYzYtNTRmNi00NTQ3LTgxZDMtZWE3N2IxNDZjNDMzIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjEiLCJuYmYiOjE3NzMxMjQxOTIsImNzcmYiOiIyYTg1MzI3My1iZmY5LTRmMDAtODAxMC1lZDY3YzMwY2UzNmQiLCJleHAiOjE3NzMxMjc3OTJ9.fE6dLAQOO5J0a5KacBypxsCQFKQ03YDZbnDov5fAZHw"

headers = {"Authorization": f"Bearer {token}"}
response = requests.get(url + "/api/profile", headers=headers)
print(response.json())
