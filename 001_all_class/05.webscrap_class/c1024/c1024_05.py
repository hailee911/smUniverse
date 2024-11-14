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

# url = 'https://new.land.naver.com/complexes/107929?ms=37.45968,126.8945045,18&a=APT:PRE:ABYG:JGC&e=RETAIL'

# browser = webdriver.Chrome()
# browser.maximize_window()
# browser.get(url)

# pyautogui.moveTo(1100,590)
# time.sleep(1)
# pyautogui.click()
# time.sleep(1)
# pyautogui.moveTo(200,700)
# time.sleep(1)
# pre_height = browser.execute_script('return articleListArea.scrollHeight')
# print('화면 높이 :',pre_height)
# while True:
#   # browser.execute_script('window.scroll(0,articleListArea.scrollHeight)')
#   pyautogui.scroll(-pre_height)
#   time.sleep(1)
#   curr_height = browser.execute_script('return articleListArea.scrollHeight')
#   if pre_height == curr_height: break
#   pre_height = curr_height
#   print("높이 :",pre_height)


# # print("-"*50)
# # all_height = browser.execute_script('return document.body.scrollHeight')
# # print("화면 전체 높이 :",all_height)

# soup = BeautifulSoup(browser.page_source,'lxml')
# data = soup.select_one('#complexOverviewList > div.list_contents > div.item_area > div')
# with open('c1024/naver.html','w',encoding='utf8') as f:
#   f.write(soup.prettify())


# 매매 낮은 5개 전세 낮은 5개 출력

# with open('c1024/naver.html','r',encoding='utf-8') as f:
#   soup = BeautifulSoup(f,"lxml")

# data = soup.select_one('#complexOverviewList > div.list_contents > div.item_area > div')
# prices = data.select('span.price')

# price_list = []
# for price in prices:
#   ps = int(price.text.strip().replace('억','').replace(',','').replace(' ','').replace('\n\n/\n\n',''))
#   price_list.append(ps)

# apts = data.select('div.item_title > span.text')

# apt_list = []
# for apt in apts:
#   ap = apt.text.strip()
#   apt_list.append(ap)

# price_list.sort(key=lambda x:x)
# print(price_list[:30])

with open(f'c1024/naver.html', 'r', encoding='utf-8') as f:
  soup = BeautifulSoup(f, 'lxml')
data = soup.select_one("#complexOverviewList > div.list_contents > div.item_area > div.item_list.item_list--article")
data_list = data.select('div.item.false')
t_mm = [] # 매매
t_gs = [] # 전세
t_ws = [] # 월세
for i in data_list:
  point = i.select_one('.item_inner > .item_link')
  name = point.select_one('.item_title > .text').text.strip().replace('\n', '')
  t_type = point.select_one('.price_line > .type').text.strip().replace('\n', '')
  money_type = point.select_one('.price_line > .price > .slash')
  if money_type == None:
    money = point.select_one('.price_line > .price').text.strip().replace('\n', '').replace('\t', '')
    if money.find('억') != -1:
      money = money.replace('억', '')
      if money.find(',') != -1:
        money += '0000'
        money = money.replace(',', '')
      else:
        money += '00000000'
        money = money.strip()
  else:
    money = point.select_one('.price_line > .price').text.strip().replace('\n', '').replace('\t', '')
    # 억 뒤에 공 0개 추가
    money_1 = money[:money.find('/')].replace(' ', '').strip()
    if money_1.find('억') != -1:
      money_1 = money_1.replace('억', '')
      if money_1.find(',') != -1:
        money_1 += '0000'
        money_1 = money_1.replace(',', '')
      else:
        money_1 += '00000000'
        money_1 = money_1.strip()
    money_2 = money[money.find('/'):].replace('/', '').strip()
  money.find(' ')
  if money in '/':
    print(money)
    print(t_type)
  if t_type == '매매':
    t_mm.append({'이름':name, '타입':t_type, '가격':int(money.replace(' ', ''))})
  elif t_type == '전세':
    t_gs.append({'이름':name, '타입':t_type, '가격':int(money.replace(' ', ''))})
  elif t_type == '월세':
    t_ws.append({'이름':name, '타입':t_type, '보증금':int(money_1.replace(' ', '')), '월세':int(money_2.replace(' ', ''))})
print(t_mm[:5])
print(t_gs[:5])
print(t_ws[:5])


