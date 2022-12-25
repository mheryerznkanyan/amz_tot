import requests
from bs4 import BeautifulSoup
from lxml import etree as et
import time
import random
import csv
import this

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
    'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8'
}

def get_amazon_price(product_url):

    try:
        response = requests.get(product_url, headers=header)
        soup = BeautifulSoup(response.content, 'html.parser')
        dom = et.HTML(str(soup))
        price = dom.xpath('//span[@class="a-price-whole"]/text()')[0]
        price_fraction = dom.xpath('//span[@class="a-price-fraction"]/text()')[0]
        return int(price), int(price_fraction)
    except Exception as e:
        return "price not available"
    
def is_available(product_url):

    try:
        response = requests.get(product_url, headers=header)
        soup = BeautifulSoup(response.content, 'html.parser')
        dom = et.HTML(str(soup))
        text = dom.xpath('//span[@class="a-size-medium a-color-success"]/text()')[0]
        if 'In Stock.' in text:
            return True
    except Exception as e:
        return "Out of stock"

def get_product_name(product_url):
    try:
        response = requests.get(product_url, headers=header)
        soup = BeautifulSoup(response.content, 'html.parser')
        dom = et.HTML(str(soup))
        name = dom.xpath('//span[@id="productTitle"]/text()')
        [name.strip() for name in name]
        return name[0]
    except Exception as e:
        return 'Not Available'
    

def is_free_shipping(product_url):
    try:
        response = requests.get(product_url, headers=header)
        soup = BeautifulSoup(response.content, 'html.parser')
        dom = et.HTML(str(soup))
        text = dom.xpath('//span[@id="price-shipping-message"]/text()')
        if 'Free Shipping' in text:
            return True
    except Exception as e:
        return  'Not Available'


product_url = 'https://www.amazon.com/ASUS-Falchion-Wireless-Mechanical-Keyboard/dp/B08T8741D5/ref=sr_1_1_sspa?keywords=gaming%2Bkeyboard&pd_rd_r=bea2b181-337f-4e96-b553-ef1be9b779b1&pd_rd_w=pslyQ&pd_rd_wg=LQX7C&pf_rd_p=12129333-2117-4490-9c17-6d31baf0582a&pf_rd_r=ABRA4V4SM13TEFYDN768&qid=1671954882&sr=8-1-spons&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzRjZMVEQ0OVVUMVpPJmVuY3J5cHRlZElkPUEwMjAxMjg5MkJOVllaSTk3M0VJUyZlbmNyeXB0ZWRBZElkPUEwMjEwNjg4MjkwR1haTUVNRTYxMCZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU&th=1'
# response = requests.get(product_url, headers=header)
# soup = BeautifulSoup(response.content, 'html.parser')
# main_dom = et.HTML(str(soup))
print(get_amazon_price(product_url))
# print(is_available(main_dom))
# print(get_product_name(main_dom))
# print(is_free_shipping(main_dom))