import requests

BASE = "Http://127.0.0.1:5000/"

response = requests.get(BASE + "helloworld/afia/29" )

print(response.json())