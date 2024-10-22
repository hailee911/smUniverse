import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/lastsearch2.naver"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status() # 에러시 종료
# soup 변환
soup = BeautifulSoup(res.text,'lxml')

data = soup.find("div",{"class":"box_type_l"})
titles = data.select("th")
names = data.select("tr>td>a")

numbers = data.select("tr>td.number")

for tit in titles:
  print(tit.text,end="\t")
print()
print("-"*100)
for idx, name in enumerate(names):
  print(f"{idx+1}\t{name.text}")

for number in numbers:
  print(number.text.strip(),end=" ")
  



