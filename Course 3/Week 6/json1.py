import urllib.request
import json

url=input('Enter location: ');
data=urllib.request.urlopen(url).read()
print('Retrieving',url)

print('Retrieved',len(data),'characters')
sum=0
info=json.loads(data)
print(info)
print('Count:',len(info["comments"]))
for item in info["comments"]:
    sum=sum+int(item["count"])

print('Sum:',sum)
