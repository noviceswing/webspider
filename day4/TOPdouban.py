from bs4 import BeautifulSoup
import requests


def bs_parse_movies(html):
    movie_list = []
    soup = BeautifulSoup(html, 'lxml')
    div_list = soup.find_all('div', class_='hd')
    for each in div_list:
        movie = each.a.span.text.strip()
        movie_list.append(movie)
    return movie_list


def get_movies():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36',
        'Host': 'movie.douban.com'
    }
    final = []
    for i in range(0, 250, 25):
        link = 'https://movie.douban.com/top250?start={}&filter='.format(i)
        r = requests.get(link, headers=headers, timeout=100)
        rep = bs_parse_movies(r.text)
        final.append(rep)
    return final


movies = get_movies()
print(movies)
