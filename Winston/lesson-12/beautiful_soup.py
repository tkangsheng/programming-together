import urllib.request as request
import urllib.parse as parse
import urllib.error as error

from bs4 import BeautifulSoup

# url = 'https://en.wikipedia.org/wiki/Animal'
url = 'http://dr-chuck.com/page1.htm'
html = request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('a')
for tag in tags:
    print(tag.get('href', None))