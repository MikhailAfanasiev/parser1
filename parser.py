import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

URL = "https://career.habr.com/vacancies/stazher"
file = "information.csv"

def parser (url = URL):
    result_list = {'href': [], 'title': [], 'overview': []}
    x = requests.get(url)
    soup = bs(x.text, "html.parser")
    names_vacancies = soup.find_all('div', class_='vacancy-card__title')
    vacancies_info = soup.find_all('div', class_='vacancy-card__skills')
    for name in names_vacancies:
        result_list['href'].append("https://career.habr.com/vacancies/stazher"+ name.a['href'])
        result_list['title'].append(name.a)
    for info in vacancies_info:
        result_list['overview'].append(info.text)
    return result_list

df = pd.DataFrame(data=parser())
df.to_csv(file)