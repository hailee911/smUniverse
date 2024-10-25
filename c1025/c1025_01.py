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

# https://www.naver.com/
# 네이버 쇼핑 검색창 입력 enter키 입력
# 네이버 쇼핑 클릭
# 네이버 쇼핑에서 무선 마우스 검색창 입력 엔터키 입력

# url = "https://www.naver.com/"
# browser = webdriver.Chrome()
# browser.maximize_window()
# browser.get(url)

# # 네이버 검색 - 입력 - 엔터
# elem = browser.find_element(By.ID,'query')
# elem.click()
# elem.send_keys('네이버 쇼핑')
# elem.send_keys(Keys.ENTER)
# time.sleep(1)
# browser.find_element(By.CLASS_NAME,'link_name').click()
# time.sleep(2)
# # 검색창 클릭, 입력, 엔터키

# original_window = browser.current_window_handle

# # 새로운 창이 열릴 때까지 대기
# WebDriverWait(browser, 10).until(EC.number_of_windows_to_be(2))

# # 모든 창 핸들 가져오기
# all_windows = browser.window_handles

# # 새로 열린 창으로 전환
# for window in all_windows:
#     if window != original_window:
#         browser.switch_to.window(window)
#         break


# elem = browser.find_element(By.CLASS_NAME,'_searchInput_search_text_3CUDs')
# elem.click()
# elem.send_keys('무선 마우스')
# elem.send_keys(Keys.ENTER)
# time.sleep(1)

# ----------------------------------------------



input("엔터")