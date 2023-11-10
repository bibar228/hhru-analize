import requests
from bs4 import BeautifulSoup
from sql_request_postgresql import sql_add, sql_del

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0"}

di = {}

for i in range(100):
    url = f"https://hh.ru/vacancies/python-backend-developer?customDomain=1&page={i}"
    src = requests.get(url, headers=headers).text

    soup_price = BeautifulSoup(src, "lxml").find_all(class_="serp-item__title")

    for j in soup_price:
        src = requests.get(j["href"], headers=headers).text
        d = BeautifulSoup(src, "lxml").find_all(class_="bloko-tag__section bloko-tag__section_text")
        skills = [i.text for i in d if len(i.text) < 15]
        print(skills)
        for d in skills:
            k = d.title()
            if k not in di:
                di[k] = 1
            else:
                di[k] += 1


sql_del()
for i, j in sorted(di.items(), key=lambda x: -x[1]):
    sql_add(i, j)


