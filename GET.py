import requests

url = 'http://localhost:5000/api/users'

response = requests.get(url)

print(response.status_code)
print(response.json())
