import requests
from base_url import base_url

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc3Mzc4NDk5NCwianRpIjoiMjE5MDZkYTMtMjNjMi00NjU1LTkzYmQtNzAyYWVmZjRlZDcyIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjEiLCJuYmYiOjE3NzM3ODQ5OTQsImNzcmYiOiIzMTZhODQ1OS1iZmQ2LTRjYTMtYTNjZS1hY2U4MzA3ZGUxY2EiLCJleHAiOjE3NzM4NzEzOTR9.BLls11u5guH4S5n256kOhu9MgUz7HCM0rEM7fdY_2aM"

headers = {"Authorization": f"Bearer {token}"}
response = requests.get(base_url + "/api/profile", headers=headers)
print(response.json())
