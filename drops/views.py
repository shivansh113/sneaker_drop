from django.shortcuts import render
import time
import re
from bs4 import BeautifulSoup
from selenium import webdriver

# Create your views here.

def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request, "index.html", {})


def scrape_result(request):
    driver = webdriver.Chrome()

    url = 'https://www.nike.com/ca/w/new-shoes-3n82yzy7ok'

    driver.get(url)


    num_scrolls = 10

    for _ in range(num_scrolls):
        # Scroll the page by going to the end of the page
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

        # Wait for the page to load after scrolling
        time.sleep(2)

    page_source = driver.page_source

    soup = BeautifulSoup(page_source, 'html.parser')

    items = soup.find_all('div', {'class': 'product-card__body'})
    prices = soup.find_all('div', {'class': 'product-card__price'})
    images = soup.find_all('a', {'class': 'product-card__img-link-overlay'})
    gender_tag = soup.find_all('div', {'class': 'product-card__titles'})

    item_store = []
    price_store = []
    image_store = []
    tag_store = []

    for item in items:
        item_store.append(item.find('a', {'class': 'product-card__link-overlay'}).text)

    for price in prices:
        price_store.append(price.find('div', {'class': 'product-price ca__styling is--current-price css-11s12ax'}).text)

    for image in images:
        
        img = str((image.find('img')))
        src_content = re.search(r'src\s*=\s*"([^"]+)"', img)
        link = src_content.group(1)
        image_store.append(link)


    for tag in gender_tag:
        tag_store.append(tag.find('div',{'class':'product-card__subtitle'}).text)


    driver.quit()

    context = {
        'items': zip(item_store, price_store, image_store, tag_store)

    }

    return render(request, 'index.html', context)