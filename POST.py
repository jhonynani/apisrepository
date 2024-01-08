import requests

url = 'http://localhost:5000/api/users'

data = {
    'username': 'nuevo_usuario',
    'email': 'nuevo_usuario@example.com'
}

response = requests.post(url, json=data)

print(response.status_code)
print(response.json())
