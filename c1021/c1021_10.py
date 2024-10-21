import requests
from bs4 import BeautifulSoup

url = "https://m.search.daum.net/search?w=tot&q=%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()

# soup 변환
soup = BeautifulSoup(res.text,'lxml')

with open("c1021/test.html","w",encoding="utf-8") as f:
  f.write(soup.prettify())

data = soup.find("c-flicking",{"id":"mor_history_id_0"})
r = data.find("c-badge-text").next
t = data.find("c-title").next
print(r)
print(t)

print("아몰랑")