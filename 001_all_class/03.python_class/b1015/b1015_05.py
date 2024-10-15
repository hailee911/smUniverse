# 학생 검색 함수

# students 리스트 타입
students = [
  {"no":1,"name":"홍길동","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":0},
  {"no":2,"name":"김관순","kor":80,"eng":80,"math":85,"total":245,"avg":81.67,"rank":0},
  {"no":3,"name":"이순동","kor":90,"eng":90,"math":91,"total":271,"avg":90.33,"rank":0},
  {"no":4,"name":"강홍찬","kor":60,"eng":65,"math":67,"total":192,"avg":64.00,"rank":0},
  {"no":5,"name":"김구","kor":100,"eng":100,"math":84,"total":284,"avg":94.67,"rank":0},
]
flag = 0
while True:
  name = input("name >> ")
  for idx, s in enumerate(students):
    if s['name'].find(name) != -1:
      print(f"{idx} 번째, {name} 학생을 찾았습니다.",s['name'])
      flag = 1

  if flag == 0:
    print("찾는 학생이 없습니다.")


ss = "파이썬 공부는 즐겁습니다. 물론 모든 공부가 다 재미있지는 않죠"
print(ss.find("공부"))
print(ss.find("자바")) # 없을때 -1
print(ss.index("공부"))
print(ss.index("자바")) # 없을때 에러

# ----------------------------------------
# 학생성적출력 함수선언

# ----------------------------------------
# 학생성적수정 함수선언



# choice = input("원하는 번호를 선택하세요. 4. >> ")
# if choice == "4":
#     pass

