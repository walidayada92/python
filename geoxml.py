import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input('Enter location: ')

count= 0
sum = 0
print('Retrieving', url)
xml = urllib.request.urlopen(url, context=ctx).read()
data=xml.decode()
print('Retrieved', len(xml), 'characters')


tree = ET.fromstring(xml)


results = tree.findall('comments/comment/count')

for item in results:
     count= count +1
     sum = sum + int(item.text)
print("Count: ", count)
print("Sum: ", sum)
