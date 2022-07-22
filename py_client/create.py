import requests

endpoint = "http://127.0.0.1:8000/api/products/"

#get_responce = requests.get(endpoint, json={"title": "Hello World"})
data = {
    "title": "Mandatory Field"
}
get_responce = requests.post(endpoint, json=data)
print(get_responce.json())
