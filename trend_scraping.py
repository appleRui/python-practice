# 取得するライブラリ
from bs4 import BeautifulSoup
import requests
# csvに保存するライブラリ
import csv
# 時間を取得するライブラリ
import datetime

# 取得するサイトURL
URL = "https://twittrend.jp/"

# URLに対してのリクエストを送り、レスポンスを取得する
responce = requests.get(URL)
# 取得するライブラリで使える形式に変換する
soup = BeautifulSoup(responce.content, 'html.parser')

# htmlのjapanという要素を取得する
japan_trend = soup.find(id="japan")
# pタグでtrendクラスの要素を取得する
trend_lists = japan_trend.find_all("p",{"class":"trend"})

# 結果の配列を入れる空配列を用意する
array = []
# for文でtrend_listsでループさせる
for trend in trend_lists:
  # 空のオブジェクトを用意
  hash = {}
  # 各trendクラスの要素のaタグの文字列を取得して、オブジェクトのtitleに格納する
  hash['title'] = trend.a.string
  # 各trendクラスの要素のaタグのhref属性を取得して、オブジェクトのlinkに格納する
  hash['link'] = trend.a.get("href") 
  # 空配列にオブジェクトに格納したものを入れる
  array.append(hash)

#　現時を取得
date_format = datetime.datetime.now()
#　時刻のフォーマットを整える
current_date = date_format.strftime("%Y%m%d%H%M")

# csvのヘッダー名を用意する
labels = ['title', 'link']

# csvにarrayの中身を書き込む
with open(f'{current_date}.csv', 'w', newline='', encoding='shift-jis') as f:
        writer = csv.DictWriter(f, fieldnames=labels)
        # ヘッダーを書き込み
        writer.writeheader()
        # for文でarrayの中身をループさせる
        for row in array:
            # 各配列の中身をcsvに書き込む
            writer.writerow(row)
# 処理終了をコンソールに出力
print(f'Saved {current_date}.csv')
