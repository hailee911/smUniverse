import requests
from bs4 import BeautifulSoup

url = "https://news.naver.com/main/ranking/popularDay.naver"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status() # 에러시 종료
# soup 변환
soup = BeautifulSoup(res.text,'lxml')
pretty = soup.prettify()

# 웹스크랩핑 web scrapping
# print(soup.find("h2",{"class":"rankingnews_tit"}))
# print(soup.select_one("h2.rankingnews_tit").text)

# print(soup.select_one("strong.rankingnews_name").text) 언론사 이름

lists = soup.find_all("a",{"class":"list_title nclicks('RBP.rnknws')"})

print("언론사 : ",soup.select_one("strong.rankingnews_name").text)
for i, li in enumerate(lists):
  if i < 5:
   print(f"{i+1}. {li.text}")
