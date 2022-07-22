import requests

endpoint = "http://127.0.0.1:8000/api/products/2/update/"

data = {
    "title": "Hello worlddddddd"
}

#get_responce = requests.get(endpoint, json={"title": "Hello World"})
get_responce = requests.put(endpoint, json=data)
print(get_responce.json())
