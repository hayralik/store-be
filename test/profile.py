import requests

url = "http://localhost:5000"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc3MzI3MDA4NCwianRpIjoiOWZjMmQ0ZjEtZGQwZS00MmFkLTkyN2MtNjUzNjEyMDM0NzI3IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjEiLCJuYmYiOjE3NzMyNzAwODQsImNzcmYiOiJiZGMzZGNkOC1jOTMyLTQ3OTMtYjg2MC0wNmEzM2I0YzMxNTMiLCJleHAiOjE3NzMzNTY0ODR9.x2P84M15kvEguqGy1L9T7rXXthHD4qxsir6OWpY6Ud8"

headers = {"Authorization": f"Bearer {token}"}
response = requests.get(url + "/api/profile", headers=headers)
print(response.json())
