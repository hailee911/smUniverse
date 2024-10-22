import requests
from bs4 import BeautifulSoup

url = "https://www.melon.com/chart/index.htm"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()  # 에러시 종료

# soup 변환
soup = BeautifulSoup(res.text, 'lxml')

# print(soup.prettify())
# 순위 사진링크주소 제목 가수명

data = soup.select_one("#frm > div > table > tbody")

ranks = data.select("span.rank") # 순위
srcs = data.select("img") # 사진링크주소
singers = data.select(".ellipsis > a") # 가수명

# for i in range(2,6):
#   print(titles[i].text)

title = []
singers = []

tits = soup.select("#lst50 > td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a") # 제목
for tit in tits:
  title.append(tit.text)
  # print(tit.text)

names = soup.select("#lst50 > td:nth-child(6) > div > div > div.ellipsis.rank02 > a") # 가수명
for name in names:
  # print(name.text)
  singers.append(name.text)

# print(title,singers)

a = singers[0]
b = singers[1]
c = a + ", " + b

# 1번째 값을 삭제
del singers[1]
singers[0] = c

w = []
for t, s in zip(title, singers):
    w.append(f"{t} - {s}")
    
print(w)

with open('c1022/melon.txt', 'w', encoding="utf-8") as f:
    for idx, line in enumerate(w):
        f.write(f"{idx+1}. {line} \n")  # 각 요소에 줄바꿈 추가