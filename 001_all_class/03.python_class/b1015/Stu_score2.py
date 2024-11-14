# = 변수 =
students = [
  {"no":1,"name":"홍길동","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":0},
  {"no":2,"name":"유관순","kor":80,"eng":80,"math":85,"total":245,"avg":81.67,"rank":0},
  {"no":3,"name":"이순신","kor":90,"eng":90,"math":91,"total":271,"avg":90.33,"rank":0},
  {"no":4,"name":"강감찬","kor":60,"eng":65,"math":67,"total":192,"avg":64.00,"rank":0},
  {"no":5,"name":"김구","kor":100,"eng":100,"math":84,"total":284,"avg":94.67,"rank":0},
]
s_title = ['번호','이름','국어','영어','수학','합계','평균','등수'] # 제목 변수
choice = 0 # 선택 변수
chk = 0    # 체크변수
count = 1  # 성적 처리 변수
stuNo = len(students)  # 학생 숫자 변수
no=0;name="";kor=0;eng=0;math=0;total=0;avg=0;rank=0 # 성적 처리 변수

# = 함수 =
def s_input(): # 1. 입력 함수
  global stuNo
  global total
  print("[ 학생 성적 입력 ]")
  while True:
    no = stuNo + 1
    name = input(f"{no}번째 학생 이름을 입력하세요. (0.이전화면) >> ")
    if name == "0":
      print("이전화면으로 돌아갑니다.")
      break
    score = []
    for i in range(3):
      s = int(input(f"{s_title[i+2]} 점수를 입력하세요. >> "))
      score.append(s)
      total += s
    avg = round(total/3, 2)
    rank = 0
    stu = {"no":no,"name":name,"kor":score[0],"eng":score[1],"math":score[2],"total":total,"avg":avg,"rank":rank}
    students.append(stu)
    stuNo += 1
    print(f"{name} 학생성적이 저장되었습니다.")
    print("♥")
    
def s_output(): # 2. 출력 함수
  print("[ 학생 성적 출력 ]")
  for i in s_title:
    print(i, end="\t")
  print()
  print("-"*60)
  for s in students:
    print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}\t{s['rank']}")
  print()

def s_modify(students):
  print("[ 학생 성적 수정 ]")
  while True:
    name = input("수정할 학생 이름을 입력하세요. (0.이전화면) >> ")
    if name == "0":
      print("이전화면으로 돌아갑니다.")
      break
    for s in students:
      if s['name'] == name:
        print(f"{name} 학생을 찾았습니다.")
        print("1. 국어")
        print("2. 영어")
        print("3. 수학")
        choice = input("수정하실 과목의 번호를 선택하세요. >> ")
        if choice == "1":
          print(f"국어 기존 성적 : {s['kor']}")
          s['kor'] = int(input("새로운 국어 점수를 입력하세요 . >> "))
          print(f"{name}학생의 성적이 수정되었습니다.")
          


# = 프로그램 시작 =
while True:
  print("[ 학생성적프로그램 ]")
  print("-"*60)
  print("1. 학생성적입력")
  print("2. 학생성적출력")
  print("3. 학생성적수정")
  print("4. 학생성적검색")
  print("5. 학생성적삭제")
  print("6. 등수처리")
  print("7. 학생성적정렬")
  print("0. 프로그램 종료")
  print("-"*60)
  choice = input("원하는 번호를 입력하세요.(0.종료)>> ")
  print()

  if choice == "1":
    s_input()
  elif choice == "2":
    s_output(students)
  elif choice == "3":
    s_modify(students)
  elif choice == "4":
    pass
  elif choice == "5":
    pass
  elif choice == "6":
    pass
  elif choice == "7":
    pass
  elif choice == "0":
    print("프로그램을 종료합니다.")
    break
# = 프로그램 종료 =