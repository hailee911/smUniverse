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

# ----------------------------------------------------------------------------------------
# selenium 화면을 숨김처리
options = Options()
options.add_argument("--headless")
options.add_argument('--window-size=1920,1080')
options.add_argument('User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36')
# ----------------------------------------------------------------------------------------
# url = 'https://www.whatismybrowser.com/detect/what-is-my-user-agent/'
# browser = webdriver.Chrome(options=options)
# browser.maximize_window()
# browser.get(url)

# soup = BeautifulSoup(browser.page_source,'lxml')
# data = soup.select_one('#detected_value').text
# print('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36')
# print(data)
# browser.get_screenshot_as_file('gmarket.png')

# input("엔터키 입력완료 >>")

# 페이지 다운
for i in range(3):
  url = f'https://www.gmarket.co.kr/n/search?keyword=%EB%85%B8%ED%8A%B8%EB%B6%81&k=61&p={i + 1}'
  wep = webdriver.Chrome(options=options)
  wep.maximize_window() # 창 최대화 (전체화면)
  wep.get(url)
  time.sleep(2)
  soup = BeautifulSoup(wep.page_source, 'lxml')
#   wep.get_screenshot_as_file(f'c1024/gmarket{i+1}.png')
  with open(f'c1024/gmarket_{i+1}', 'w', encoding='utf-8') as f:
    f.write(soup.prettify())


for i in range(3):
    with open(f'c1024/gmarket_{i+1}', 'w', encoding='utf-8') as f:
        soup = BeautifulSoup(f,"lxml")
    data = soup.select_one('#section__inner-content-body-container > div:nth-child(4)')
    lists = data.select('#section__inner-content-body-container > div:nth-child(4) > div:nth-child(1)')
    print(len(lists))



# 노트북 검색 된 사이트 1,2,3페이지에서
# 만족도 95 이상이면서, 평가수 100명 이상, 금액 150만원 이하

# data = soup.select('#section__inner-content-body-container > div:nth-child(4) > div:nth-child(1)')
# print(len(data))
