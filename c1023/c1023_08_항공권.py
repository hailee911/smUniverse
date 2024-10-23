from selenium import webdriver
from selenium.webdriver.common.by import By as by
from selenium.webdriver.common.keys import Keys as keys
import time
import requests, random
from bs4 import BeautifulSoup
# url = 'https://www.naver.com'
url = 'https://flight.naver.com'
browser = webdriver.Chrome()
browser.maximize_window() # 창 최대화 (전체화면)
browser.get(url)
# 출발지 선택
elem = browser.find_element(by.XPATH, '//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[1]/button[1]/b')
elem.click()
time.sleep(1)
# 김포 입력
elem = browser.find_element(by.CLASS_NAME, 'autocomplete_input__qbYlb')
elem.send_keys('김포')
time.sleep(1)
# 김포 공항 선택
elem = browser.find_element(by.XPATH, '//*[@id="__next"]/div/main/div[8]/div[2]/section/ul/li[2]/a/b')
elem.click()
time.sleep(1)
# 도착지 선택
elem = browser.find_element(by.XPATH, '//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[1]/button[2]')
elem.click()
time.sleep(1)
# 제주 입력
elem = browser.find_element(by.XPATH, '//*[@id="__next"]/div/main/div[8]/div[1]/div/input')
elem.send_keys('제주')
time.sleep(1)
# 제주 선택
elem = browser.find_element(by.XPATH, '//*[@id="__next"]/div/main/div[8]/div[2]/section/ul/li/a/b')
elem.click()
time.sleep(1)
# 출발 날짜
elem = browser.find_element(by.XPATH, '//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[2]/button[1]')
elem.click()
time.sleep(1)
elem = browser.find_element(by.XPATH, '//*[@id="__next"]/div/main/div[8]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr[2]/td[4]/button')
elem.click()
time.sleep(1)
# 도착 날짜
elem = browser.find_element(by.XPATH, '//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[2]/button[2]')
elem.click()
time.sleep(1)
elem = browser.find_element(by.XPATH, '//*[@id="__next"]/div/main/div[8]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr[2]/td[7]/button')
elem.click()
time.sleep(1)
# 인원 선택
elem = browser.find_element(by.XPATH, '//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[3]/button')
elem.click()
time.sleep(1)
elem = browser.find_element(by.XPATH, '//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[4]/div/div/div[1]/div[1]/button[2]')
elem.click()
time.sleep(1)
# 항공권 검색
elem = browser.find_element(by.XPATH, '//*[@id="__next"]/div/main/div[2]/div/div/div[2]/button[1]')
# elem = browser.find_element(by.XPATH, '//*[@id="__next"]/div/main/div[2]/div/div/div[2]/button[1]/span')
elem.click()
elem.click()
# 검색중 (화면대기)
# time.sleep(7)
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# 화면 대기
# 화면에 찾을려고 하는 <html> 요소
# 에러남 . 질문해야함
elem = WebDriverWait(browser, 120).until(lambda x: x.find_element(by.XPATH,'//*[@id="__next"]/div/main/div[4]/div/div[2]'))
print(elem)
time.sleep(10)
# 화면 스크롤 내리기
while True:
  # 현재 스크롤 높이 검색
  prev_height = browser.execute_script('return document.body.scrollHeight')
  print('최초 높이 : ', prev_height)
  # 스크롤 내리기
  browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
  time.sleep(2) # 다른정보가 추가될때까지 대기
  # 높이 확인
  curr_height = browser.execute_script('return document.body.scrollHeight')
  if prev_height == curr_height:
    break
  prev_height = curr_height
  print('현재 높이 : ', curr_height)
    # 중지
    # 다르면 반복
# 데이터 가져와서 처리
# BeautifulSoup 데이터 처리
# 웹 스크래핑으로 데이터 가져오기
soup = BeautifulSoup(browser.page_source, 'lxml')
with open('flight.html', 'w', encoding='utf-8') as f:
  f.write(soup.prettify())
input('enter 키를 입력하면 프로그램이 종료합니다. ')
browser.quit()
# # 네이버항공권 페이지 이동
# elem = browser.find_element(by.ID, 'query')
# elem.send_keys('네이버 항공권')
# elem.send_keys(keys.ENTER)
# # 네이버항공권 선택
# elem = browser.find_element(by.CLASS_NAME, 'link_name')
# elem.click()
time.sleep(100)