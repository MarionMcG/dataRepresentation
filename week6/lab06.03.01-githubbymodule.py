# Going to do this lab with my aithentication code, instead of Andrew's
# His code returned a 400 error, probably because someone uploaded it to github

## curl -i -H "Authorization: token ad2489f9c8f2dfe48e22d07f8a42efc2191be62c" 
# https://api.github.com/user/repos works, for now. 

import requests
from github import Github

g = Github("ad2489f9c8f2dfe48e22d07f8a42efc2191be62c")
#print list of repos
##print(Repositories)
##for repo in g.get_user().get_repos():
   ##print(repo.name)


repo = g.get_repo("MarionMcG/dataRepresentation")
#print("\nClone URL for dataRepresentation:", repo.clone_url)


fileInfo = repo.get_contents("README.md")
urlOfFile = fileInfo.download_url
#print ("Download URL for Data Representation README.md:", urlOfFile)

response = requests.get(urlOfFile)
contentOfFile = response.text
#print (contentOfFile)

newContents = contentOfFile + "\n o/ This line was added, as part of Lab 3 in Week 6 \n"
#print (newContents)

gitHubResponse=repo.update_file(fileInfo.path,"updated by prog",newContents,fileInfo.sha)
print (gitHubResponse)