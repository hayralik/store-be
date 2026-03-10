import requests

url = "http://localhost:5000"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc3MzAwMjE2OSwianRpIjoiYzQxYTg2M2MtMjUwNS00ODVlLThlNTYtODU0Yjc3NmQ0MTIzIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjEiLCJuYmYiOjE3NzMwMDIxNjksImNzcmYiOiIyZmJhNDMzOS03Zjg5LTQ4NjktODE0NC1iNDlkNWU3NTRjMmUiLCJleHAiOjE3NzMwMDMwNjl9.-IhGQaZ5X4PTObQNzVVv9KO5H-bDKLiOzoevudyeqCs"

headers = {"Authorization": f"Bearer {token}"}
response = requests.get(url + "/api/profile", headers=headers)
print(response.json())
