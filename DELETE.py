import requests

user_id = 1  # Reemplaza con el ID del usuario que deseas eliminar
url = f'http://localhost:5000/api/users/{user_id}'

response = requests.delete(url)

print(response.status_code)
print(response.json())
