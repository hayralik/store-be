import requests

url = "http://localhost:5000"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc3MzE1MzEyMiwianRpIjoiMTFkOGNjOGYtZDZjMC00YzllLWJiZjktZTUyOWY1ZWZjMzIyIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjEiLCJuYmYiOjE3NzMxNTMxMjIsImNzcmYiOiIxZWVhMmE2OS1lMDNkLTQxODQtOTZmZC0xYmVhZWVjYTU3YmEiLCJleHAiOjE3NzMyMzk1MjJ9.uPcHD3G0GoWVeSUehSSnj9ZpUNDeVLS_etNsX2fywn0"

headers = {"Authorization": f"Bearer {token}"}
response = requests.get(url + "/api/profile", headers=headers)
print(response.json())
