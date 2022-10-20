import random
import requests
import csv
from bs4 import BeautifulSoup


def get_content(url):
    header = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:105.0) Gecko/20100101 Firefox/105.0'}

    timeout = random.choice(range(80, 100))

    while True:
        rep = requests.get(url, headers=header, timeout=timeout)
        rep.encoding = 'utf-8'
        break

    return rep.text


def get_data(html_text):
    final = []
    bs = BeautifulSoup(html_text, "html.parser")
    body = bs.body
    data = body.find_all('div', {'class': 'quote'})
    # print('************************************************************')
    # print(data)
    for single in data:
        temp = []
        text = single.find('span', {'class': 'text'}).string
        author = single.find('small').string
        temp.append(text)
        temp.append(author)
        final.append(temp)

    return final


def write_data(data, name):
    file_name = name
    with open(file_name, 'a', errors='ignore', newline='') as f:
        f_csv = csv.writer(f)
        f_csv.writerows(data)


if __name__ == '__main__':
    for i in range(1, 11):
        url = 'https://quotes.toscrape.com/page/{}/'.format(i)
        html = get_content(url)
        result = get_data(html)
        write_data(result, 'Quotes.csv')
