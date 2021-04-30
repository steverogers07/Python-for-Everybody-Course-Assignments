import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import string

url=input('Enter - ')
html=urllib.request.urlopen(url).read()
soup=BeautifulSoup(html, 'html.parser')

count=int(input('Enter Count: '))
pos=int(input('Enter Position: '))

name=None
while(count):
    tags=soup('a')
    tag=tags[pos-1]
    name=tag.contents[0]
    url=tag.get("href",None)
    print('Retrieving:',url)
    html=urllib.request.urlopen(url).read()
    soup=BeautifulSoup(html, 'html.parser')
    count=count-1;

print(name)
