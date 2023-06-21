
from selenium import webdriver
from bs4 import BeautifulSoup
import time


driver = webdriver.Chrome()

url = 'https://www.nike.com/ca/w/new-shoes-3n82yzy7ok'

driver.get(url)

num_scrolls = 5 

for i in range(num_scrolls):
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    time.sleep(1.5)

page_source = driver.page_source

soup = BeautifulSoup(page_source, 'html.parser')

items = soup.find_all('div', {'class': 'product-card__body'})
prices = soup.find_all('div', {'class': 'product-card__price'})

item_store = []
price_store = []

for item in items:
  item_store.append(item.find('a', {'class': 'product-card__link-overlay'}).text)

for price in prices:
  price_store.append(price.find('div', {'class': 'product-price ca__styling is--current-price css-11s12ax'}).text)


for i in range(len(item_store)):
  print(i+1,': ', item_store[i], " ", price_store[i])

import requests 
from bs4 import BeautifulSoup

url = 'https://www.nike.com/ca/w/shoes-y7ok?q=jordan'

site = requests.get(url)
soup = BeautifulSoup(site.text, 'html.parser')

items = soup.find_all('div', {'class': 'product-card__body'})
prices = soup.find_all('div', {'class': 'product-card__price'})

item_store = []
price_store = []

for item in items:
  item_store.append(item.find('a', {'class': 'product-card__link-overlay'}).text)

for price in prices:
  price_store.append(price.find('div', {'class': 'product-price ca__styling is--current-price css-11s12ax'}).text)


for i in range(len(item_store)):
  print(i+1,': ', item_store[i], " ", price_store[i])
