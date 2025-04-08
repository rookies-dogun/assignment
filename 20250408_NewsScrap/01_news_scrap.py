import requests
from lxml import html

url = 'https://news.daum.net/economy'

response = requests.get(url)
response.raise_for_status()

tree = html.fromstring(response.content)

xpath = '//*[@id="0e289a02-ba69-440a-8a28-2b0479c64993"]/ul/li[1]/a/div[2]/strong'
title_element = tree.xpath(xpath)

if title_element:
    print("뉴스 제목:", title_element[0].text_content().strip())
else:
    print("")