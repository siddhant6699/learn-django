import requests

endpoint = "http://127.0.0.1:8000/api/"

#get_responce = requests.get(endpoint, json={"title": "Hello World"})
get_responce = requests.post(endpoint, json={"title": "Hello World"})
print(get_responce.json())
