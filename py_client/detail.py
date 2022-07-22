import requests

endpoint = "http://127.0.0.1:8000/api/products/2/"

#get_responce = requests.get(endpoint, json={"title": "Hello World"})
get_responce = requests.get(endpoint)
print(get_responce.json())
