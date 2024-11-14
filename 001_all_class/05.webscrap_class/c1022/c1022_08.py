import requests
from bs4 import BeautifulSoup
url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=1=9&backgroundColor="
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
    'Accept-Language':'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7'}
res = requests.get(url,headers=headers)
res.raise_for_status() # 에러시 종료
soup = BeautifulSoup(res.text,"lxml")
# 제목,금액,평점,평가수,링크주소,이미지주소
# 기준점
data = soup.select_one("#productList")

lists = data.select("li")
n_lists = []
for idx,list in enumerate(lists):
  n_list = [] # 제목,금액,평점,평가수,링크,이미지
  try:
    price = int(list.select_one("strong.price-value").text.replace(",",""))
    rating = float(list.select_one("em.rating").text)
    num = int(list.select_one("span.rating-total-count").text[1:-1])
    # 금액 평점 평가수 비교
    if price >= 900000 and rating >= 4.5 and num >= 500:
      print(f"[{idx} 번째 ]")
      print("1. 링크주소 :","https://www.coupang.com"+list.select_one("a")['href'])
      print("2. 제목 :",list.select_one("div.name").text)
      print("3. 금액 :",price)
      print("4. 평점 :",rating)
      print("5. 평가수 :",num)
      print("-"*50)
      # n_list.append(list.select_one("div.name").text)
      n_list.append(price)
      n_list.append(rating)
      n_list.append(num)
      n_lists.append(n_list)
  except:
    pass
                  

print(n_lists)

# while True:
#   print("[ 노트북 비교 ]")
#   print("1. 금액정렬")
#   print("2. 금액역순정렬")
#   print("3. 평점정렬")
#   print("4. 평점역순정렬")
#   print("0. 종료")
#   print("-"*50)
#   choice = input("원하는 번호를 입력하세요.")

  # if choice == "1":
  #   print("금액정렬 : ",n_list.sort(key=lambda x:x[0]))

  # elif choice == "2":
  #   pass