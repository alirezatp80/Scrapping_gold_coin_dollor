import requests
from bs4 import BeautifulSoup
import re
from decimal import Decimal

def formating(title , price:str):
    num = price.replace(',','')
    price = format(Decimal(num)/10 , ',')
    
    print(f'{title} => {(price)}')
    

url_crypto = 'https://www.tgju.org/crypto'


def crypto(url):
    r = requests.get(url)

    soup = BeautifulSoup(r.text , "html.parser")

    result = soup.find_all('tr',attrs={'data-market-nameslug':re.compile(r'crypto-(bitcoin)$|(ethereum)$|(tether)$') })
    for i in result:
        title = i.find('span' , class_ = 'original-title-en').text
        price = i.find('div' , attrs={'data-market-p':f'crypto-{str(title).lower()}-irr'}).text
        formating(title , price)
    
url_currency = 'https://www.tgju.org/currency'
def currency(url):
    r = requests.get(url)
    
    soup = BeautifulSoup(r.text , 'html.parser')
    result = soup.find_all('tr' , attrs={'data-market-nameslug':re.compile(r'price_((kwd)|(dollar_rl)|(eur)|(bhd)|(omr)|(gbp)|(chf))')})
    for i in result:
        title = i.find('th').text
        price = i.find('td' , class_ = 'nf').text
        formating(title , price)

url_gold='https://www.tgju.org/'
def gold_coin(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text , 'html.parser')
    result = soup.find_all('ul' , class_ = 'info-bar')
    for i in result:
        mini_result = i.find_all('li' , attrs={'id':re.compile(r'(l-geram18)|(l-sekee)|(l-oil_brent)')})
        for j in mini_result:
            title = j.find('h3').text
            price = j.find('span', class_="info-price").text
            formating(title , price)
gold_coin(url_gold)
crypto(url_crypto)
currency(url_currency)
