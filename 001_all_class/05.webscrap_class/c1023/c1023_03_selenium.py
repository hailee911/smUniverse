from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup
import time

# chrome() ()안에 chromedriver.exe 위치 지점을 입력해줘야
# root에 파일이 저장되어 있으면 입력하지 않아도 됨.

browser = webdriver.Chrome()
browser.get("https://naver.com")

# html 위치 찾기
elem = browser.find_element(By.CLASS_NAME,'MyView-module__link_login___HpHMW')

elem.click()

browser.forward()
browser.refresh()
elem = browser.find_element(By.NAME,'pw')

elem = browser.find_element(By.ID,'query')
elem.send_keys("네이버 영화")
elem.send_keys(Keys.ENTER)

# 새창이동
browser.switch_to.window(browser.window_handles[0])

time.sleep(10)
