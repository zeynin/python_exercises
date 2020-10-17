#http://www.practicepython.org/exercise/2014/06/06/17-decode-a-web-page.html

from bs4 import BeautifulSoup
import requests
import webencodings
from html5lib import html5lib


url = 'http://www.nytimes.com/'
r = requests.get(url)
r_html = r.text

# some requests code here for getting r_html 

soup = BeautifulSoup(r_html,'features="html5lib"')
title = soup.find('span', 'articletitle').string
print(soup.get_text())
