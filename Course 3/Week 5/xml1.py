import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET


url=input('Enter location: ')
xml=urllib.request.urlopen(url).read()
print('Retrieving',url)

print('Retrived',len(xml),'characters')
sum=0
info=ET.fromstring(xml)
lst=info.findall('comments/comment')
for item in lst:
    sum=sum+int(item.find('count').text)
print('Count:',len(lst))
print('Sum:',sum)
