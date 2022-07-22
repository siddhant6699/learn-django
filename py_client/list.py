import requests

endpoint = "http://127.0.0.1:8000/api/products/"

get_responce = requests.get(endpoint)
print(get_responce.json())
