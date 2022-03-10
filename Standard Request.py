# https://www.geeksforgeeks.org/python-web-scraping-tutorial/

import requests
from bs4 import BeautifulSoup
import re

# page is a request object
base_url = 'https://www.goodreads.com/book/show/9222475-infernal-devices'
page = requests.get(base_url)

# print(page.__dict__)
# print(page.status_code, page.text, page.url)
# print(page.content)


souped_page = BeautifulSoup(page.content, 'html.parser')
# print(souped_page.prettify())
# print(souped_page.title)
# print(souped_page.title.parent.name)

# s = souped_page.find('span', class_="Text Text_body3")
# print(s)

# content = s.find_all('p')
tags = souped_page.find_all('<span class="Formatted">')
print(tags)


page_num = souped_page.find_all(text='pages')
# print(page_num)
