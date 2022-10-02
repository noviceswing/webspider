import requests
import csv
from bs4 import BeautifulSoup
import time
import random

def get_page(url):
    header = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:105.0) Gecko/20100101 Firefox/105.0'}

    timeout = random.choice(range(80, 100))

    while (True):
        rep = requests.get(url, headers=header, timeout=timeout)
        rep.encoding = 'utf-8'
        break
    
    return rep.text

def get_data(html_text):
    final = []
    bs = BeautifulSoup(html_text, "html.parser")
    body = bs.body
    data = body.find('div', {'id':'7d'})
    ul = data.find('ul')
    li = ul.find_all('li')

    for day in li:
        temp = []
        date = day.find('h1').string
        temp.append(date)     
        inf = day.find_all('p')
        temp.append(inf[0].string)

        if inf[1].find('span') is None:
            temperture_highest = None
        
        else:
            temperture_highest = inf[1].find('span').string
            temperture_lowest = inf[1].find('i').string
            temp.append(temperture_highest)
            temp.append(temperture_lowest)

            final.append(temp)

    return final

def write_data(data, name):
    filename = name
    with open (filename, 'w', errors='ignore', newline='') as f:
        f_csv = csv.writer(f)
        f_csv.writerows(data)

if __name__=='__main__':
    url = 'http://www.weather.com.cn/weather/101271101.shtml'
    html = get_page(url)
    result = get_data(html)
    write_data(result, 'yibinweatheragain.csv')
