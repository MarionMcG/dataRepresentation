# curl -i -H "Authorization: tokenb55d312da577ba479f7dc4f8f3f5b1384bdf3b2e" https://api.github.com/user/repos
#Returns 401 unauthorised at the time of my attempt

#7. Checking info on my own github
# curl -i -H "Authorization: token ad2489f9c8f2dfe48e22d07f8a42efc2191be62c" https://api.github.com/user/repos works



# Get data from my public dataRepresentation repo
import requests 
import json

apikey = 'ad2489f9c8f2dfe48e22d07f8a42efc2191be62c'
url = 'https://api.github.com/repos/MarionMcG/dataRepresentation'
filename = "repo.json"

response = requests.get(url, auth=('token',apikey))
repoJSON = response.json()
#print (response.json())
file = open(filename, 'w')
json.dump(repoJSON, file, indent=4)