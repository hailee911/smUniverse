import requests
from bs4 import BeautifulSoup

url = "https://www.11st.co.kr/browsing/BestSeller.tmall?method=getBestSellerMain&xfrom=main^gnb"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()

# soup 변환
soup = BeautifulSoup(res.text,'lxml')
soup.prettify()

# title = soup.find("div",{"id":"bestPrdList"})
# print(title.find("h3").text)

# name = soup.find("li",{"id":"thisClick_6019941174"})
# print(name.find("p").text)

rank = soup.find("div",{"id":"bestPrdList"}).find("ul",{"class":"cfix"})
lists = rank.find_all("li") # 28개

for idx, list in enumerate(lists):
  p_tit = list.find("div",{"class":"pname"}).p.text
  p_price = list.find("strong",{"class":"sale_price"}).text
  print(f"{idx+1}. {p_tit}, 금액 : {p_price} 원")



