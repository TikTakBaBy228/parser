from bs4 import BeautifulSoup
import urllib.request

req = urllib.request.urlopen('https://mirnov.ru/lenta-novostej')
html = req.read()

soup = BeautifulSoup(html, 'html.parser')
news = soup.find_all('article', class_='col-12 col-sm-6 mb-5')
results = []

for item in news:
    title = item.find('figcaption', class_='little').get_text(strip=True)
    desc = item.find('header', class_='slavecon-title mt-1').get_text(strip=True)
    href = item.a.get('href')
    results.append({
        'title': title,
        'desc': desc,
        'href': href,
    })

f = open('news.txt', 'w', encoding='utf-8')
i = 1
for item in results:
    f.write(f'Новость № {i}\n\nНазвание: {item["title"]}\nОписание: {item["desc"]}\nСсылка: {item["href"]}\n\n**************************\n')
    i += 1
f.close()