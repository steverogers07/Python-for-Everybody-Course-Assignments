import urllib.request, urllib.parse, urllib.error
import json

api='http://py4e-data.dr-chuck.net/json?'
address=input('Enter location: ')
parms = dict()
parms['address'] = address
parms['key'] = 42
url=api+urllib.parse.urlencode(parms)

print('Retrieving ',url)
uh = urllib.request.urlopen(url)
data = uh.read().decode()
print('Retrieved',len(data),'characters')
js=json.loads(data)
print('Place id',js["results"][0]["place_id"])
