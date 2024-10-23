from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random
import requests
from bs4 import BeautifulSoup

url = "https://www.daum.net/"

# 크롬 브라우저 열기
browser = webdriver.Chrome()
# 네이버 페이지 이동
browser.get(url)
# 로그인버튼 선택
elem = browser.find_element(By.CLASS_NAME,"btn_login")
# 로그인버튼 클릭
elem.click()

id = "01057468335"
pw = "1111"
input_js = f'document.getElementById("loginId--1").value="{id}";\
  document.getElementById("password--2").value="{pw}";'

browser.execute_script(input_js)

time.sleep(random.randint(2,5))
elem = browser.find_element(By.CLASS_NAME,"btn_g")
elem.click()

time.sleep(100)