from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('http://py4e-data.dr-chuck.net/comments_38193.html')
html = urlopen(url, context=ctx).read()

soup = BeautifulSoup(html, "html.parser")
tags = soup('span')
for tag in tags:
    # Look at the parts of a tag
    print('TAG:', tag)
    print('URL:', tag.get('href', None))
    print('Contents:', tag.contents[0])
    print('Attrs:', tag.attrs)




#for line in f:
#    num = re.findall("[0-9]+", line)
#    for i in num:
#    total = total + number
#    number = 0
#print (total)
