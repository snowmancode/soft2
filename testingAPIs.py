import requests

the_response = requests.get(url="http://http://api.open-notify.org/iss-now.json")

print(the_response)
print(response.status_code)

txt = "Welcome to my Kingdom"

a = txt.split()

print(a)