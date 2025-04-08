from bs4 import BeautifulSoup
import requests

url = 'https://news.daum.net/economy'  
response = requests.get(url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'html.parser')

strong_tags = soup.select("ul.list_newsheadline2 > li > a > div.cont_thumb > strong.tit_txt")

for tag in strong_tags:
    print(tag.getText(strip=True))