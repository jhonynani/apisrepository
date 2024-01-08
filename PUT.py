import requests

user_id = 1  # Reemplaza con el ID del usuario que deseas actualizar
url = f'http://localhost:5000/api/users/{user_id}'

data = {
    'username': 'nuevo_nombre',
    'email': 'nuevo_email@example.com'
}

response = requests.put(url, json=data)

print(response.status_code)
print(response.json())
