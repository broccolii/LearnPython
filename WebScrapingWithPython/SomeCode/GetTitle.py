from bs4 import BeautifulSoup
import urllib.request
from urllib.error import HTTPError
from urllib.request import urlopen

# try:
#     html = urlopen('http://www.python.org/fish.html')
# except HTTPError as e:
#     print(e.code)
# else:
#     bsObj = BeautifulSoup(html.read(), 'html.parser')
#     print(bsObj.h1)

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None

    try:
        bsObj = BeautifulSoup(html.read(), 'html.parser')
        title = bsObj.h1
    except AttributeError as e:
        return None
    return title

title = getTitle('http://www.python.org/fish.html')

if title == None:
    print('Title could not be found')
else:
    print(title)