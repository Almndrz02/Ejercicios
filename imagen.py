import requests
import sys

'''configurar la consola para usar UTF-8'''
sys.stdout.reconfigure(encoding='utf-8')

url = "https://dog.ceo/api/breeds/image/random"

'''realizar la solicitud a la API'''
response = requests.get(url)

'''Verificar si la solicitud fue exitosa'''
if response.status_code == 200:
    # Obtener los datos en formato JSON
    data = response.json()
    print(f"Aquí tienes una imagen de un perro:\n{data['message']}")

else:
    print("Hubo un problema al obtener la imagen.")
