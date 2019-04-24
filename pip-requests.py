import requests

requests_website = requests.get("https://pypi.org/project/requests/")

print(requests_website.status_code)

print(requests_website.content)

print(requests_website.headers)



