from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import csv
import time
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
import pyautogui

# 제목 금액 평점 평가수 찜 1-5페이지
# 평점 4.8이상, 평가수 1000명이상 인 상품을 csv파일로 저장하고 출력하시오.
# ------------------------------------------------------------------------
# wep = webdriver.Chrome() 

# for i in range(1,6):
  # 웹사이트 5개 가져와서 shopping_i.html 파일로 저장
  # url = f"http://search.shopping.naver.com/search/all?adQuery=%EB%AC%B4%EC%84%A0%20%EB%A7%88%EC%9A%B0%EC%8A%A4&origQuery=%EB%AC%B4%EC%84%A0%20%EB%A7%88%EC%9A%B0%EC%8A%A4&pagingIndex={i}&pagingSize=40&productSet=total&query=%EB%AC%B4%EC%84%A0%20%EB%A7%88%EC%9A%B0%EC%8A%A4&sort=rel&timestamp=&viewType=list"
  # wep.get(url)
  # time.sleep(3)
  # soup = BeautifulSoup(wep.page_source,'lxml')
  # with open(f'c1025/shopping_{i}.html','w',encoding='utf8') as f:
  #   f.write(soup.prettify())
# ------------------------------------------------------------------------
# # 파일저장하기 - 강사님 ver
# browser = webdriver.Chrome()
# browser.maximize_window()
# time.sleep(3)
# for i in range(1):
#   url = f"https://search.shopping.naver.com/search/all?adQuery=%EB%AC%B4%EC%84%A0%EB%A7%88%EC%9A%B0%EC%8A%A4&origQuery=%EB%AC%B4%EC%84%A0%EB%A7%88%EC%9A%B0%EC%8A%A4&pagingIndex={i+5}&pagingSize=40&productSet=total&query=%EB%AC%B4%EC%84%A0%EB%A7%88%EC%9A%B0%EC%8A%A4&sort=rel&timestamp=&viewType=list"
#   browser.get(url)
#   time.sleep(2)
#   # # 화면을 스크롤해서 내리기 반복
#   prev_height = browser.execute_script("return document.body.scrollHeight")
#   while True:
#     browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
#     time.sleep(1)
#     # 페이지가 로딩되면서 길어진 길이를 다시 가져옴.
#     curr_height = browser.execute_script("return document.body.scrollHeight")
#     # 페이지를 스크롤해서 길이가 더 길어졌는지 확인
#     if prev_height == curr_height:
#       break
#     # 더 길이가 길어졌으면, 이전길이에 현재길이를 입력시킴
#     prev_height = curr_height
#   print("스크롤 내리기 완료")
#   soup = BeautifulSoup(browser.page_source,"lxml")
#   with open(f'c1025/navershop5.html','w',encoding='utf-8') as f:
#     f.write(soup.prettify())
#   time.sleep(2)
# ------------------------------------------------------------------------
# 제목 금액 평점 평가수 찜 1-5페이지
# 평점 4.8이상, 평가수 1000명이상 인 상품을 csv파일로 저장하고 출력하시오.

# 저장된 파일 읽어오기 -> 리스트에 추가
p_info = []
for i in range(1,6):
  with open(f'c1025/navershop{i}.html','r',encoding='utf8') as f:
    soup = BeautifulSoup(f,'lxml')
  # 기준점
  data = soup.select_one('#content > div.style_content__xWg5l > div.basicList_list_basis__uNBZx > div')
  lists = data.select('div.product_item__MDtDF')
    
  # name = data.select_one('div.product_title__Mmw2K').text.strip()

  # 제품 가격 별점 가져와서 출력
  for list in lists:
    name = list.select_one('div.product_title__Mmw2K > a').text.strip()
    price = list.select_one('span.price_num__S2p_v>em').text.strip()
    # 별점 체크
    rating_element = list.select_one('span.product_grade__IzyU3')

    # None 체크 및 기본값 설정 (지피티)
    if rating_element:
        rating_text = rating_element.text.replace('별점', '').replace('\n', '').strip()
        # 숫자 또는 소수점 여부 체크
        if rating_text.replace('.', '', 1).isdigit():  # '.' 하나는 허용
            rating = float(rating_text)
        else:
            rating = 0
    else:
        rating = 0

    # print(f'별점: {rating}')

    num_element = list.select_one('span.product_num__fafe5')
    if num_element:
        num_text = num_element.text.replace('별점', '').replace('\n', '').strip()
        # 숫자 또는 소수점 여부 체크
        if num_text.replace(',', '',1).isdigit():
            num = int(num_text.replace(',',''))
        else:
            num = 0
    else:
        num = 0
    
    # 별점 float 찜 int
    print(f"제품: {name}, 가격: {price}, 별점: {rating}, 찜: {num}")
    p_info.append(name)
    p_info.append(price)
    p_info.append(rating)
    p_info.append(num)

# 평점 4.8이상, 평가수 1000명이상 인 상품을 csv파일로 저장하고 출력하시오.
print(p_info)

# ------------------------------------------------------------------------
# 1.상단타이틀. csv파일로 저장
with open('c1025/shopping.csv', 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['제품', '가격 (원)', '별점', '찜'])

# 4개씩 잘라서 출력
    for i in range(0, len(p_info), 4):
        writer.writerow(p_info[i:i+4])   
