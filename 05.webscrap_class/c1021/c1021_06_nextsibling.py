# import requests
# from bs4 import BeautifulSoup

# url = "https://news.naver.com/main/ranking/popularDay.naver"
# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}
# res = requests.get(url,headers=headers)
# res.raise_for_status()
# soup = BeautifulSoup(res.text, "lxml")

# print("타이틀 : ", soup.find("strong",{"class":"rankingnews_name"}).text)

# print(soup.find("a",{"class":"list_title nclicks('RBP.rnknws')"}).text)


import requests
from bs4 import BeautifulSoup

url = "https://news.naver.com/main/ranking/popularDay.naver"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

# 첫 번째 타이틀
first_title = soup.find("strong", {"class": "rankingnews_name"}).text
print("타이틀 : ", first_title)

# 모든 a 태그 가져오기
titles = soup.find_all("a", {"class": "list_title nclicks('RBP.rnknws')"})
# 첫 번째와 두 번째 타이틀 출력
if len(titles) > 1:
    print("두 번째 타이틀 : ", titles[1].text)
else:
    print("두 번째 타이틀이 없습니다.")



