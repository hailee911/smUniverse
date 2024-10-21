import requests
from bs4 import BeautifulSoup

url = "https://news.naver.com/main/ranking/popularDay.naver"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
# print(soup.div)

# 특정정보출력
# print(soup.find("div",attrs={"id":"header"}))
# print(soup.find("div",{"id":"header"})) # div 태그 id = "header"
# print(soup.find("h2",{"class":"rankingnews_tit"}).text) # h2 태그 class = "rankingnews_tit"의 text를 출력
# print(soup.find_all("div")) # 모든 div 태그 검색 
# print(len(soup.find_all("div"))) # 모든 div 태그 개수 출력
# print(type(soup.find_all("div"))) # 모든 div 태그 타입

# print(soup.find("div",{"class":"rankingnews_box_wrap"}))

# find : 1개 검색
rankingnews_wrap = soup.find("div",{"class":"rankingnews_box_wrap"})
# find_all : 여러개 검색
rankingnews_boxs = rankingnews_wrap.find_all("div",{"class":"rankingnews_box"})
print(len(rankingnews_boxs))

print(soup.find("strong",{"class":"rankingnews_name"}).text)
# soup.find("div",{"class":"rankingnews_box_wrap"}).find()

# print(len(soup.find_all("div",{"class":"rankingnews_box"})))

newLists = soup.find("div",{"class":"rankingnews_box_wrap"}).find_all("div",{"class":"rankingnews_box"})

print("여러개 개수 확인 : ",len(newLists))

for newList in newLists:
  print(newList.find("strong",{"class":"rankingnews_name"}).text)

  print(1,"="*20)
  print(newList)
  print(2,"="*20)
# next : 검색태그 다음뒤에 오는 태그를 찾아줌
# next_sibling : 검색태그의 형제관계의 다음태그를 찾아줌
  print(newList.next_sibling.next_sibling)


print("여러개 개수 확인 : ",len(newList))