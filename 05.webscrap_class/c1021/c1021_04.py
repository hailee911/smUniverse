import requests
from bs4 import BeautifulSoup

url = "https://news.naver.com/main/ranking/popularDay.naver"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()

with open("c1021/1.html","w",encoding="utf8") as f:
  f.write(res.text)

# html,css 정보를 가진 소스변경
soup = BeautifulSoup(res.text,'lxml') # str -> html태그, css태그 사용될 수 있는 형태로 변경

# BeautifulSoup 사용
# 태그 출력, 태그 글자 출력
print(soup.title) # <title>랭킹뉴스 : 네이버 뉴스</title> title 태그 출력
print(soup.title.text) # 랭킹뉴스 : 네이버 뉴스 title 태그 문자열을 출력

print("없는 태그 : ",soup.titletitle) # 없는 태그 시 None
# print("없는 태그 : ",soup.titletitle.get_text()) # 없는 태그 시 에러남
print(soup.a.next.text) # next - 다음 태그를 가져옴.
# 태그 속성 출력
print(soup.a.attrs) # 태그의 속성값 가져옴 : 딕셔너리 형태
print(soup.a["href"]) # a 태그의 href 속성값을 가져옴

# soup.prettify() 정보 저장
# with open("c1021/2.html","w", encoding="utf8") as f:
#   # soup.prettyify() : 소스가 정리되어 저장됨.
#   f.write(soup.prettify())

print("완료!")

# print(res.text)