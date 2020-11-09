import requests

URL = "https://www.monster.ca/jobs/search/?q=Marketing-Co__2Dordinator&where=Vancouver__2C-British-Columbia"
page = requests.get(URL)

f = open("demo.txt", "w")
f.write(str(page.content))
f.close()