from fileinput import filename
import requests
from bs4 import BeautifulSoup
import csv
class Webspider():
    def __init__(self) -> None:
        self.url = 'https://movie.douban.com/cinema/nowplaying/beijing/'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
        }
        r = requests.get(self.url,headers=self.headers)
        r.encoding = r.apparent_encoding
        self.html = r.text

    def beautiful_find(self):
        """
            利用beautiful进行解析        
        """
        _final = []
        bs = BeautifulSoup(self.html, 'lxml')
        titles = bs.find_all('li', class_='list-item')
        for each in titles:
            temp = []
            title = each['data-title']
            temp.append(title)
            _final.append(temp)
        return _final

    def write_data(self, data, name):
        filename = name
        with open (filename, 'w', errors='ignore') as f:
            f_csv = csv.writer(f)
            f_csv.writerows(data)

if __name__ == "__main__":
    webspider = Webspider()
    data = webspider.beautiful_find()
    webspider.write_data(data, 'douban.csv')