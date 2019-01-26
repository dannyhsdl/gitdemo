from bs4 import BeautifulSoup
import requests
myweb=requests.get("https://www.baidu.com").content
soup=BeautifulSoup(myweb,"html.parser")
links=soup.findAll('a')
print(soup.text)
# print(links)
for l in links:
    print(l)
    print(l.text)


