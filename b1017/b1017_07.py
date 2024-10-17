members = []
m_title = ['id','pw','name','nicName','address','money']

f = open('b1017/member.csv',"r",encoding="utf-8")
while True:
  line = f.readline()
  if not line:break
  m = line.strip().split(",")
  m[5] = int(m[5])
  members.append(dict(zip(m_title,m)))

f.close()

def m_search(members):
  # 아이디 검색
  # members 딕셔너리에서
  # 입력한 문자로 검색된 데이터 모두 출력하시오.
  # (a가 들어가있는 아이디를 출력)
  mid = input("아이디를 입력하세요.>> ")
  for m in members:
    if mid in m['id']:
      print(m)

def m_register(members):
  id = input("id를 입력하세요.>> ")
  for m in members:
    if m['id'] == id:
      print(f"{id} 와 동일한 아이디가 있습니다. 다시 입력하세요.")
      flag = 1
      if flag == 1:
        return False
      else:
        print(f"{id} 는 사용가능합니다.")
        continue
  pw = input("pw를 입력하세요.>> ")
  name = input("이름을 입력하세요.>> ")
  nicName = input("닉네임을 입력하세요.>> ")
  money = int(input("충전금액을 입력하세요.>>"))
  m_list = [id,pw,name,nicName,money]
  members.append(dict(zip(m_title,m_list)))
  print(f"{id} 님 회원가입이 완료되었습니다!")
  print(m_list)

def sign_in(members):
  chk = 0
  id = input("아이디 >> ")
  pw = input("비밀번호 >> ")
  for m in members:
    if m['id'] == id and m['pw'] == pw:
      print("로그인에 성공했습니다.")
      chk = 1
      main_shop()
    elif chk == 0:
      print("아이디 혹은 비밀번호가 틀렸습니다.")
      break

def main_shop():
    while True:
      print("           [ SM-SHOP ]")
      for m in members:
        
        print(f"                       닉네임:{m['nicName']}님")
        print(f"                       금액 :{m['money']:,} 원")
      print("1. 삼성TV - 2,000,000")
      print("2. LG냉장고 - 3,000,000")
      print("3. 하만카돈스피커 - 500,000")
      print("4. 세탁기 - 1,000,000")
      print("7. 내용저장")
      print("8. 구매내역 ")
      print("9. 금액충전 ")
      break
      # choice = int(input("구매하려는 상품번호를 입력하세요.>> "))


while True:
  print("1. 회원등록")
  print("2. 회원검색")
  print("3. 로그인")
  choice = input("원하는 번호를 입력하세요.>> ")
  if choice == "1":
    m_register(members)

  elif choice == "2":
    m_search(members)
  elif choice == "3":
    sign_in(members)
    










  
