import requests

user_id = 1  # Reemplaza con el ID del usuario que deseas obtener
url = f'http://localhost:5000/api/users/{user_id}'

response = requests.get(url)

print(response.status_code)
print(response.json())
