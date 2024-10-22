import requests
from bs4 import BeautifulSoup

url = "https://www.melon.com/index.htm"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()

# soup 변환
soup = BeautifulSoup(res.text,'lxml')

with open("c1021/test.html","w",encoding="utf-8") as f:
  f.write(soup.prettify())

# tit = soup.find("ul",{"class":"sub_list"}).find("span",{"class":"title"}).text
# singer = soup.find("dl",{"class":"ml0"}).find("span",{"class":"ellipsis"}).text
# print(tit)
# print(singer)

lists = soup.find("li",{"class":"issue_list04"})
# print(lists)
# print(lists.find("span",{"class":"title"}))
# print(lists.find("span",{"class":"ellipsis"}))

# for idx, list in enumerate(lists):
t = lists.find("a",{"class":"mlog link-thumb"})
# s = lists.find("span",{"class":"ellipsis"}).text

print(t)
  # print(idx+1,".",t ,"-", s)