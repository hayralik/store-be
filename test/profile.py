import requests
from base_url import base_url

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc3Mzc4NTU2MywianRpIjoiY2E4ZmMwYmYtMjEwZi00MTUxLWJhMDUtYzJiMjBkM2VkMDhhIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjIiLCJuYmYiOjE3NzM3ODU1NjMsImV4cCI6MTc3Mzg3MTk2M30.WWQah2P3VegPjcKeKjN4VLmOUskqbftaKeI8ilmTNvk"

headers = {"Authorization": f"Bearer {token}"}
response = requests.get(base_url + "/api/profile", headers=headers)
print(response.json())
