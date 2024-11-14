# 멜론 투표

from selenium import webdriver
from selenium.webdriver.common.by import By as by
from selenium.webdriver.common.keys import Keys as keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = 'https://www.melon.com/melonaward/weekAward.htm'
browser = webdriver.Chrome()
browser.maximize_window() # 창 최대화 (전체화면)
browser.get(url)

browser.find_element(by.XPATH, '//*[@id="timeline-wrap"]/div[3]/div[1]/div[4]/div/div[2]/div[2]/div[2]/button').click()
browser.find_element(by.XPATH, '//*[@id="conts_section"]/div/div/div[1]/a').click()

# 현재 열려 있는 모든 창의 핸들을 가져옴
original_window = browser.current_window_handle
browser.find_element(by.XPATH, '//*[@id="conts_section"]/div/div/div[1]/a').click()

# 모든 창의 핸들을 가져온 후 새 창으로 전환
for window_handle in browser.window_handles:
    if window_handle != original_window:
        browser.switch_to.window(window_handle)
        break

try:
    # 요소가 로드될 때까지 대기
    time.sleep(1)  # 혹은 WebDriverWait을 사용할 수 있음
    browser.find_element(by.XPATH, '//*[@id="mainContent"]/div/div/form/div[4]/button[2]').click()
    time.sleep(5)
except Exception as e:
    print(f"오류 발생: {e}")

time.sleep(2)
# browser.find_element(by.CLASS_NAME, 'd_vote d_click_log_area').click()

# 필요한 작업이 끝난 후 원래 창으로 돌아가기
# browser.switch_to.window(original_window)  # 원래 창으로 돌아가기

browser.switch_to.window(original_window)

# 원래 창에서 특정 요소 클릭
try:
    # 요소가 로드될 때까지 대기
    vote_area = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((by.XPATH, '//*[@id="timeline-wrap"]/div[3]/div[1]/div[4]/div/div[2]/div[2]/div[2]/button'))
    )
    vote_area.click()
except Exception as e:
    print(f"오류 발생: {e}")

time.sleep(100)
