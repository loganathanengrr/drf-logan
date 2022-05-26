import requests

endpoint = "https://httpbin.org/status/200/"
endpoint = "http://127.0.0.1:8000/api/"

response = requests.get(endpoint, params={"abc":123}, json={"query":"Hello World"}) # HTTP Request

# print(response.text) # raw text response


print(response.json()) # JSON response