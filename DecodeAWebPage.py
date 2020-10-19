#http://www.practicepython.org/exercise/2014/06/06/17-decode-a-web-page.html

import requests
from bs4 import BeautifulSoup


url = 'http://www.nytimes.com/'
r = requests.get(url)

# some requests code here for getting r_html 

soup = BeautifulSoup(r.text, 'html.parser')

for title in soup.titles
    print('title = ' + title)
