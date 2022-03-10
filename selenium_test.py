# https://www.youtube.com/watch?v=onlQ7fL4ey8
from selenium import webdriver

driver = webdriver.Firefox()
driver.get('https://www.goodreads.com/book/show/9222475-infernal-devices')

html = driver.page_source
print(html)
