import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/lastsearch2.naver"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()  # 에러시 종료

# soup 변환
soup = BeautifulSoup(res.text, 'lxml')

data = soup.select_one("#contentarea>div.box_type_l>table")
stocks = data.select("tr")

# 상단타이틀 출력
tits = stocks[0].select("th")
title = []
for tit in tits:
  title.append(tit.text)
  print(tit.text,end="\t")
print()
print("_"*120)

# print(stocks[1])

# 주식 30개 출력 - 5개 출력
st_lists = []
for i in range(2,50):
  st_list = []
  sts = stocks[i].select("td")
  if len(sts) <= 1: continue # td가 1개 이하이면 제외
  for idx, st in enumerate(sts):
    s = ""
    if idx == 4:
      s = st.select_one("span").text
      s += st.select_one("span").next.next.next.text.strip()
      print(st.select_one("span").text, end="")
      print(st.select_one("span").next.next.next.text.strip(), end="\t")
    else:
      s = st.text.strip()
      print(st.text.strip(), end="\t")
    st_list.append(s)
  st_lists.append(st_list)
  print()
  print("_"*120)

print(title)
print(st_lists)

# stock.txt 파일에 저장하시오.

# with open('c1022/stock.txt','w',encoding="utf-8") as f:

title = ['순위', '종목명', '검색비율', '현재가', '전일비', '등락률', '거래량', '시가', '고가', '저가', 'PER', 'ROE']

a = ",".join(title)+"\n"
print(a)
with open('c1022/stock.txt','w',encoding="utf-8") as f:
  f.write(a)
