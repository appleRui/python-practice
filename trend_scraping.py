from bs4 import BeautifulSoup
import requests
import csv
import datetime

URL = "https://twittrend.jp/"

reaponce = requests.get(URL)
soup = BeautifulSoup(reaponce.content, 'html.parser')

japan_trend = soup.find(id="japan")
trend_lists = japan_trend.find_all("p",{"class":"trend"})

array = []
for trend in trend_lists:
  hash = {}
  hash['title'] = trend.a.string
  hash['link'] = trend.a.get("href") 
  array.append(hash)

date_format = datetime.datetime.now()
current_date = date_format.strftime("%Y%m%d%H%M")

labels = ['title', 'link']

with open(f'{current_date}.csv', 'w', newline='', encoding='shift-jis') as f:
        writer = csv.DictWriter(f, fieldnames=labels)
        writer.writeheader()
        for row in array:
            writer.writerow(row)

print(f'Saved {current_date}.csv')