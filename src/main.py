import requests

respose = requests.get("https://api.github.com")
print(respose.json())