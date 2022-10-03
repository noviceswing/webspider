import random
import requests
import time 
import csv
from bs4 import BeautifulSoup

def get_content(url):
    header = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:105.0) Gecko/20100101 Firefox/105.0'}

    timeout = random.choice(range(80,100))

    while True:
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
    print(li)
    for day in li:
        temp = []
        date = day.find('h1').string
        temp.append(date)
        inf = day.find_all('p')
        temp.append(inf[0].string)

        if inf[1].find('span') is None:
            temperature_highest = None
        
        else:
            temperature_highest = inf[1].find('span').string

            temperature_lowest = inf[1].find('i').string

            temp.append(temperature_highest)
            temp.append(temperature_lowest)
            
            final.append(temp)
    return final        

def write_data(data, name):
    file_name = name 
    with open(file_name, 'w', errors='ignore', newline='') as f:
        f_csv = csv.writer(f)
        f_csv.writerows(data)

if __name__ == '__main__':
    url = 'http://www.weather.com.cn/weather/101271101.shtml'
    html = get_content(url)
    result = get_data(html)
    write_data(result, 'yibinweather.csv')
