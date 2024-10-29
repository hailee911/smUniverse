import requests
import csv
import time
from bs4 import BeautifulSoup
url = "https://finance.naver.com/sise/lastsearch2.naver"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
    'Accept-Language':'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7'}
res = requests.get(url,headers=headers)
res.raise_for_status() # 에러시 종료
soup = BeautifulSoup(res.text,"lxml")
# print(soup.prettify())

data = soup.select_one("#productList")

# 기준점
data = soup.select_one("#contentarea > div.box_type_l > table")
stocks = data.select("tr")
print(len(stocks))

# 1. 상단타이틀 항목 : 12개
st_list = [st.text for st in stocks[0].select("th")]
f = open('c1023/a.csv','w',encoding='utf-8-sig',newline="")
writer = csv.writer(f)
writer.writerow(st_list)
# print(st_list)

# 2.
# print(stocks[1].select("td")) # 항목 : 1개
# print(len(stocks[2].select("td"))) # 항목 12개

# sto_list = [sto.text.strip().replace("\t","").replace("\n","") for sto in stocks[2].select("td")]
# print(sto_list)
# sto_list = [sto.text.strip().replace("\t","").replace("\n","") for sto in stocks[3].select("td")]
# print(sto_list)

# 30개 주식정보를 csv파일로 저장하시오.

# sto_list = [sto.text.strip().replace("\t","").replace("\n","") for sto in stocks[46].select("td")]
# print(sto_list)


# sto_list = []
# for i in range(len(stocks)):
#   for sto in stocks[i].select("td"):
#     sto_list.append(sto.text.strip().replace("\t","").replace("\n",""))

# sto_list = [item for item in sto_list if item]  # 빈 문자열 제거
# writer.writerow(sto_list)

# print(sto_list)


# 리스트 생성
# sts = stocks[0].select("th")
# st_list = []
# for st in sts:
#   print(st.text, end="\t")
#   st_list.append(st.text)

# print(st_list)


# 30개 주식정보를 csv파일로 저장하시오.
print(len(stocks)) # 50개
for stock in stocks:
  sts = stock.select("td")
  if len(sts) <= 1: continue
  sto_list = [ st.text.strip().replace("\t","").replace("\n","")  for st in sts ]
  writer.writerow(sto_list)
  print(sto_list)

    