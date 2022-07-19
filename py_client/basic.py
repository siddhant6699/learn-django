import requests

endpoint = "http://127.0.0.1:8000/api/"

get_responce = requests.get(endpoint, json={"query": "Hello World"})
print(get_responce.text)
print(get_responce.status_code)
print(get_responce.json)
