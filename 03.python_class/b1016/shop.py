import datetime
member = [
  {"id":"aaa", "pw":"1111", "name": "이다영", "nicName":"nana", "address":"서울특별시", "money": 1000000000},
  {"id":"bbb", "pw":"2222", "name": "권순영", "nicName":"hoshi", "address":"대구광역시", "money": 1000000000},
  {"id":"ccc", "pw":"3333", "name": "이석민", "nicName":"dk", "address":"부산시", "money": 1000000000 },
  {"id":"ddd", "pw":"4444", "name": "최한솔", "nicName":"vernon", "address":"뉴욕", "money": 1000000000},
  {"id":"admin", "pw":"5555", "name": "윤정한", "nicName":"zzong", "address":"인천시", "money": 1000000000},
]
m_keys = ['id','pw','name','nicName','address','money']
# member.txt 파일 읽기, member딕셔너리 저장
f = open('b1016/member.txt','r',encoding='utf-8')
while True:
  line = f.readline()
  if not line: break
  m = line.strip().split(",")
  m[5] = int(m[5])
  member.append(dict(zip(m_keys,m)))
print(member)

# cart.txt파일 읽기, member딕셔너리 저장
# print(f"{c['cno']}\t{c['id']}\t{c['name']}\t{c['pCode']}\t{c['pName']:14s}\t{c['price']}\t{c['date']}")
cartNo = 0
cart = []
c_keys = ["cno","id","name","pCode","pName","price","date"]
f = open('b1016/cart.txt','r',encoding='utf-8')
while True:
  line = f.readline()
  if not line: break
  c = line.strip().split(",")
  c[0] = int(c[0])
  c[5] = int(c[5])
  cart.append(dict(zip(c_keys,c)))
f.close()
# ========================================

session_info = {}
product = [
  {'no':1,'pCode':'t001','pName':'삼성TV  ','price':2000000, 'color':'black'},
  {'no':2,'pCode':'g001','pName':'LG냉장고','price':3000000, 'color':'white'},
  {'no':3,'pCode':'b001','pName':'Bang&Olufsen','price':5000000, 'color':'silver'},
  {'no':4,'pCode':'w001','pName':'LG세탁기','price':1000000, 'color':'gray'},
]
cartNo = 0
cart = []
p_title = ['번호','아이디','이름','상품코드','상품명','가격','구매일자']

# # # # 함수 선언 # # # # 
def buy(choice):
  global cartNo
  print(f"{product[choice-1]['pName']} 를 구매하셨습니다.")
  print("구매내역에 등록합니다.")
  print()
  now = datetime.datetime.now()
  today = now.strftime("%Y-%m-%d %H:%M:%S")
  c = {"cno":cartNo+1,"id":session_info['id'],"name":session_info['name'],"pCode":product[choice-1]['pCode'],"pName":product[choice-1]['pName'],"price":product[choice-1]['price'],"date":today}
  session_info['money'] -= product[choice-1]['price']
  cart.append(c)
  
  cartNo += 1
  # return cartNo - buy(choice,cartNo)

def buy_output():
  # 구매내역 출력
    print(f"{p_title[0]}\t{p_title[1]}\t{p_title[2]}\t{p_title[3]}\t{p_title[4]}\t\t{p_title[5]}\t{p_title[6]}")
    sum = 0
    for c in cart:
      sum += c['price']
      print(f"{c['cno']}\t{c['id']}\t{c['name']}\t{c['pCode']}\t\t{c['pName']:10s}\t{c['price']}\t{c['date']}")

    print("-"*50)
    print(f"총 구매 금액: {sum}")
    print(f"총 구매 건수: {len(cart)}")
def money():
  # 금액충전
    print("[ 금액 충전 ]")
    print(f"현재 금액 : {session_info['money']}")
    money = int(input("충전하실 금액을 입력하세요.>> "))
    session_info['money'] += money
    print(f"충전된 금액 : {session_info['money']}")

def buy_save():
  # member.txt 파일생성해서 내용을 저장하시오.
  f = open('b1016/member.txt','w',encoding='utf-8')
  for m in member:
    f.write(f"{m['id']},{m['pw']},{m['name']},{m['nicName']},{m['address']},{m['money']}\n")
  f.close()
  # member.txt 파일생성해서 내용을 저장하시오.
  f = open('b1016/cart.txt','w',encoding='utf-8')
  for c in cart:
    f.write(f"{c['cno']},{c['id']},{c['name']},{c['pCode']},{c['pName']},{c['price']},{c['date']}\n")
  f.close()
  print("내용저장이 완료되었습니다.")
  print()


# # # # 프로그램 시작 # # # #
while True:
  print("[ 로그인 ]")
  input_id = input("아이디를 입력하세요.>>")
  input_pw = input("패스워드를 입력하세요.>>")
  # db에서 가져옴.
  # member 데이터를 가지고 비교
  flag = 0
  for m in member:
    if input_id == m['id'] and input_pw == m['pw']:
      print("SM SHOP에 오신것을 환영합니다!")
      session_info = m
      print("-"*50)
      flag = 1
      break
  if flag == 0:
    print("아이디 또는 패스워드가 일치하지 않습니다.")
  else:
    break

while True:
  print("-"*50)
  print("        [ SM-SHOP ]")
  print(f"                        닉네임: {session_info['nicName']}님")
  print(f"                        금액: {session_info['money']:,} 원")
  print("1. 삼성TV - 2,000,000")
  print("2. LG냉장고 - 3,000,000")
  print("3. Bang & Olufsen - 5,000,000")
  print("4. LG세탁기 - 1,000,000")
  print("8. 구매내역 ")
  print("9. 금액충전")
  choice = int(input("구매하려는 상품번호를 입력하세요.>> "))
  print("-"*50)

  if choice == 1:
    buy(choice)
  elif choice == 2:
    buy(choice)
  elif choice == 3:
    buy(choice)
  elif choice == 4:
    buy(choice)
  elif choice == 7:
    buy_save()
  elif choice == 8:
    buy_output()
  elif choice == 9:
    money()
    
    