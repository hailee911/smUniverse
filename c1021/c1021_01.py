# web crawling - 웹 크롤러가 웹 상에 존재하는 컨텐츠를 수집하는 작업
# web scrapping - 원하는 정보를 추출하여 수집하는 기술
# pip install requests - 웹 정보 요청하는 라이브러리
# pip install beautifulsoup4 - html/xml 파일에서 원하는 데이터를 parsing 할 수 있는 라이브러리
# pip install lxml - css 문법으로 특정 요소를 쉽게 가져올 수 있는 python 라이브러리
# extension : open in browser

import requests
res = requests.get("http://www.google.com/") # html 소스를 가져옴.
res = requests.get("http://www.naver.com/") # html 소스를 가져옴.
# res = requests.get("https://www.melon.com/chart/index.htm") # -> #406 에러
# res.raise_for_status() # 에러시 종료
# requests 정보를 가져올 시 제이쿼리, 자바스크립트, 외부페이지 react, vue.. 비동기식으로 (소스는 가져오지 못함.)
print("총 문자 길이 : ",len(res.text))

# 파일 저장
# f = open("c1021/a.html","w",encoding="utf-8")
# f.write(res.text)
# f.close()

# # f.close()
# with open("b.html","w",encoding="utf-8") as f:
#   f.write(res.text)


# if res.status_code == 200:
#   print(res.text)
# else:
#   print("접근할 수 없습니다.")

# print("응답코드 : ",res.status_code) # 200

# print(res.text)
