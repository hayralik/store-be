import requests

url = "http://localhost:5000"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc3MzQ3MzQ2MywianRpIjoiMTY0OWQyZTUtNTllYy00YzBmLWFhYmItMTI0ZWFjNDU2NzBjIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjEiLCJuYmYiOjE3NzM0NzM0NjMsImNzcmYiOiJmNzg3MWNkMC1hNTcxLTRjNmMtOTJhZC0yODFkNmMwN2Y2YmIiLCJleHAiOjE3NzM1NTk4NjN9.t1s_Naerf7uY62RL2sQiyuotKS1SFsryQAG5Ns-HK6M"

headers = {"Authorization": f"Bearer {token}"}
response = requests.get(url + "/api/profile", headers=headers)
print(response.json())
