# [ 영화순위 ]
# 1. 2020년~2023년 영화 내용을 저장하시오.
# - csv파일로 저장
# - 이미지 저장
# - 제목
# - 관객수 : 숫자입력
# 1,312 -> 1312
# - 날짜
# 2. DataFrame 변경
# 관객수
# -> 최대값
# -> 최소값
# -> 평균
# -> 최대관객수 5개
# -> 최소관객수 5개를
# 출력하시오.

from selenium import webdriver
import time
import requests
from bs4 import BeautifulSoup
url = 'https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q=2023%EB%85%84+%EC%98%81%ED%99%94+%EC%88%9C%EC%9C%84'

# 다음 웹사이트를 html 파일로 저장해두고 soup으로 가져오기
# browser = webdriver.Chrome()
# browser.get(url)
# time.sleep(2)
# soup = BeautifulSoup(browser.page_source, "lxml")

# with open(f'd1106/daum.html','w',encoding='utf8') as f:
#   f.write(soup.prettify())

# 웹 스크래핑
with open(f'd1106/daum.html','r',encoding='utf8') as f:
  soup = BeautifulSoup(f,'lxml')

data = soup.select_one("#mor_history_id_0 > div > div.flipsnap_view > div > div:nth-child(1) > c-flicking-item > c-layout > div")
titles = data.select("strong>a")

counts = data.select("c-contents-desc > p > a")

dates = data.select("c-contents-desc-sub > span")

for i in range(len(titles)):
  print(titles[i].text.strip())
  print(int(counts[i].text.strip()[2:-2].replace(',', '').replace(' ', '') + '0000'*1))
  print(dates[i].text.strip())


# 데이터프레임 생성 -> csv 파일
import csv

# Open a CSV file for writing
with open('movies.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    
    # Write the header (optional)
    writer.writerow(['제목', '관객수', '날짜'])

    # Loop through the lists and write each row
    for i in range(len(titles)):
        title = titles[i].text.strip()
        count = int(counts[i].text.strip()[2:-2].replace(',', '').replace(' ', '')+'0000'*1)
        date = dates[i].text.strip()

        # Write the extracted data into the CSV file
        writer.writerow([title, count, date])

        # Print the output for verification
        print(title)
        print(count)
        print(date)
