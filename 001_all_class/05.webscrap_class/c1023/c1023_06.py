from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random
import requests
from bs4 import BeautifulSoup

url = "http://www.naver.com"

# 크롬 브라우저 열기
browser = webdriver.Chrome()
# 네이버 페이지 이동
browser.get(url)
# 로그인버튼 선택
elem = browser.find_element(By.CLASS_NAME,"MyView-module__link_login___HpHMW")
# 로그인버튼 클릭
elem.click()
time.sleep(random.randint(2,5))

# 자바스크립트 호출방법
id = "idy0911"
pw = "naver0911"
input_js = f'document.getElementById("id").value = "{id}";\
  document.getElementById("pw").value = "{pw}";'

browser.execute_script(input_js)

time.sleep(random.randint(2,5))

# 로그인 버튼 클릭
elem = browser.find_element(By.CLASS_NAME,"btn_login")
elem.click()

time.sleep(100)
# -------------------------------------------------------------

# # id값을 입력
# elem = browser.find_element(By.ID,"id")
# elem.send_keys("idy0911")
# time.sleep(random.randint(2,5))

# elem = browser.find_element(By.ID,"pw")
# elem.send_keys("naver0911")
# time.sleep(random.randint(2,5))

# 로그인 버튼 클릭
# elem = browser.find_element(By.CLASS_NAME,"btn_login")
# elem.click()

