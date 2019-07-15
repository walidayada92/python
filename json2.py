import json
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input('Enter location: ')

counter= 0
sum = 0
print('Retrieving', url)
xml = urllib.request.urlopen(url, context=ctx).read()
data=xml.decode()

info = json.loads(data)
print('Retrieved', len(info), 'characters')


for item in info["comments"]:
     counter= counter +1
     sum = sum + int(item['count'])

print("Count: ", counter)
print("Sum: ", sum)
