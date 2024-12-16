import requests
import validators

url = "https://api.github.com"

if validators.url(url):
    try:
        response = requests.get(url)
        response.raise_for_status() # raise an HTTPError for bad responses (4xx and 5xx)
        print(response.json())
    except requests.exceptions.RequestException as e: 
        print(f"An error occurred: {e}")
else:
    print("Invalid URL.")
