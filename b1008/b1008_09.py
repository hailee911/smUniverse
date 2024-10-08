# students 리스트 타입
students = [
  {"no":1,"name":"홍길동","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":0},
  {"no":2,"name":"유관순","kor":80,"eng":80,"math":85,"total":245,"avg":81.67,"rank":0},
  {"no":3,"name":"이순신","kor":90,"eng":90,"math":91,"total":271,"avg":90.33,"rank":0},
  {"no":4,"name":"강감찬","kor":60,"eng":65,"math":67,"total":192,"avg":64.00,"rank":0},
  {"no":5,"name":"김구","kor":100,"eng":100,"math":84,"total":284,"avg":94.67,"rank":0},
]
s_title = ['번호','이름','국어','영어','수학','합계','평균','등수'] #전역변수
choice = 0 # 전역변수
chk = 0    # 체크변수
count = 1  # 성적처리
stuNo = len(students)  # 리스트에 학생이 있으면, 그 인원으로 변경
no=0;name="";kor=0;eng=0;math=0;total=0;avg=0;rank=0 #성적처리변수

# 학생성적프로그램
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

  if choice == 1:
    while True:
      print("[ 학생 성적 입력 ]")
      # 학생 성적 직접 입력
      print()
      no = stuNo + 1 # 리스트 -> 학생 수 1부터
      name = input(f"{no}번째 학생 이름을 입력하세요. (0. 이전 화면으로) >> ")
      if name == "0":
        print("성적 입력을 취소합니다.")
        print()
        break # 빠져나오기 -> 상단 메뉴로
      kor = int(input("국어 점수를 입력하세요. >>"))
      eng = int(input("영어 점수를 입력하세요. >>"))
      math = int(input("수학 점수를 입력하세요. >>"))
      print("★")
      total = kor + eng + math
      avg = round(total / 3, 2)
      rank = 0
      students.append([no, name, kor, eng, math, total, avg, rank])
      stuNo += 1 # 학생 수 1 증가
      print(f"{name}학생의 성적이 저장되었습니다.")
      print("★")

  elif choice == "2":
    print("***")
    print("[ 학생 성적 출력 ] ")
    print()
    print(s_title)
    print("-"*60)
    for stu in students:
      for s in stu:
        print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']}\t{s['rank']}") 
      print()
    print()
    print("***") 

  elif choice == "2":
    print("[ 학생 성적 수정]")
    name = input("수정하고자 하는 학생 이름을 적어주세요. >>")

  elif choice == "7":
    while True:
      print("[ 학생 성적 정렬 ]")
      print("1. 이름 순차 정렬")
      print("2. 이름 역순 정렬")
      print("3. 합계 순차 정렬")
      print("4. 합계 역순 정렬")
      print("5. 번호 순차 정렬")
      print("0. 이전페이지 이동")
      print("-"*40)
      choice == input("원하는 번호를 입력하세요. >> ")

      if choice == "1":
        students.sort(key=lambda x:x['name'])
      elif choice == "2":
        students.sort(key=lambda x:x['name'], reverse=True)
      elif choice == "0":
        print("이전 페이지로 이동합니다.")
        break
      print("정렬이 완료되었습니다.")








