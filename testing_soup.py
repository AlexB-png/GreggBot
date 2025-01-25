import bs4 as BeautifulSoup

html_doc = """
< p class="title"><b>The Dormouse's story</b></ p>
< p class="story">Once upon a time there were three little sisters; and their names were <a id="link1" class="sister" href="http://example.com/elsie">Elsie</a>, <a id="link2" class="sister" href="http://example.com/lacie">Lacie</a> and <a id="link3" class="sister" href="http://example.com/tillie">Tillie</a>; and they lived at the bottom of a well.< /p>
< p class="story">...< /p>
"""
soup = BeautifulSoup.BeautifulSoup(html_doc, 'html.parser')

for link in soup.find_all('a'):
    print(link.get('href'))

    
import re

huggg_p_link="https://launch.huggg.me/"

x = re.findall(huggg_p_link)

def striphtml(data):
    p = re.compile(r'<.*?>')
    return p.sub('', data)
print(striphtml(html_doc))