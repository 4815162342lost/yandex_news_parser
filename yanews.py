#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup
r=requests.get("http://yandex.ru")

"""old version
soup=BeautifulSoup(r.text, "html.parser")
news=soup.find_all(class_="home-link list__item-content home-link_black_yes")
print("Global news:")
for new_cur in news[0:10]:
        print(new_cur.get("aria-label"))
print("\nCity news:")
for new_cur in news[10:20]:
        print(new_cur.get("aria-label"))
"""
        
soup=BeautifulSoup(r.text, "html.parser")
news=soup.find_all(class_="news__item-content")

print("Russian news:")
for current_news in news:
    print(current_news.text)
