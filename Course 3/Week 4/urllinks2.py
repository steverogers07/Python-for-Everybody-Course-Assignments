import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url=input('Enter - ')
html=urllib.request.urlopen(url).read()
soup=BeautifulSoup(html, 'html.parser')

sum=0
count=0
tags=soup('span')
for tag in tags:
    sum=sum+int(tag.contents[0])
    count=count+1

print('Count',count)
print('Sum',sum)
