import urllib.request, urllib.parse, urllib.error,xml.etree.ElementTree as ET,requests
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
print('Receiving :',url)


tree = ET.fromstring(requests.get(url).text)
counts=tree.findall('.//count')

print('Retrieved:',len(tree))
sum=0
for i in counts:
        y=int(i.text)
        
        sum+=y
       
print(sum)
