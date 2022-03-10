from turtle import title
from selenium import webdriver
from bs4 import BeautifulSoup
import re

class BookInfo:

    def __init__(self, title: str, author: str, page_num: int, description: str, genres: list, publish_date: str) -> None:
        self.title = title
        self.author = author
        self.page_num = page_num
        self.descripton = description
        self.genres = genres
        self.publish_date = publish_date

def tagText(tag_search):
    tag = tag_search
    try:
        print(tag.text)
        return tag.text
    except:
        print('Tag not found')
        return 'error'

driver = webdriver.Firefox()
driver.get('https://www.goodreads.com/book/show/9222475-infernal-devices')
souped_page = BeautifulSoup(driver.page_source, 'html.parser')


page_num = tagText(souped_page.find('span', itemprop='numberOfPages'))
page_num = page_num.rstrip(' pages')
# page_num = souped_page.find('span', itemprop='numberOfPages')
# page_num = page_num.text.rstrip(' pages')
try:
    page_num = int(page_num)
except:
    page_num = 0

author = tagText(souped_page.find('span', itemprop='name'))

title = tagText(souped_page.find('h1', id='bookTitle'))
title = title.strip('\n')
title = title.strip(' ')


description = souped_page.find('div', id='descriptionContainer')
print(description)