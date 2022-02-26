# Use the request library
import requests
# set the target webpage
url = 'http://192.168.63.167/snow'
r = requests.get(url)
# This will get the full page
print(r.text)

# This will get the status code
print("***************************")
print("Status Code:")
print("\t*",r.status_code)
print("***************************")

# This will just get the headers
h = requests.head(url)
print("Header:")
print("***************************")
# To print line by line
for x in h.headers:
    print("\t",x,":",h.headers[x])
print("***************************")

# This will modify the headers user-agent
headers = {
    'User-Agent':'Mobile'
}

rh = requests.get(url,headers=headers)
print(rh.text)