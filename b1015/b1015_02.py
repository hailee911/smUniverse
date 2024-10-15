# students 리스트 타입
students = [
  {"no":1,"name":"홍길동","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":0}
]
s_title = ['번호','이름','국어','영어','수학','합계','평균','등수'] #전역변수
choice = 0 # 전역변수
chk = 0    # 체크변수
count = 1  # 성적처리
stuNo = len(students)  # 리스트에 학생이 있으면, 그 인원으로 변경
no=0;name="";kor=0;eng=0;math=0;total=0;avg=0;rank=0 #성적처리변수

# 학생성적입력 함수 확인
def stu_input():
  global stuNo
  while True:
    print("[ 학생 성적 입력 ]")
    no = stuNo + 1
    name = input(f"{no}번째 학생이름을 입력하세요. (0.이전화면으로 이동) >> ")
    if name == "0":
      print("이전 화면으로 이동합니다.")
      print()
      break
    score = []
    for i in range(3):
      k = int(input(f"{s_title[i+2]} 점수를 입력하세요. >> "))
      total += k
      score.append(k)

    # kor = int(input("국어 점수를 입력하세요. >> "))
    # eng = int(input("영어 점수를 입력하세요. >> "))
    # math = int(input("수학 점수를 입력하세요. >> "))
    # total = kor+eng+math

    avg = round(total/3 , 2)
    rank = 0

    s = {"no":no, "name":name, "kor":score[0], "eng":score[1], "math":score[2], "total":total, "avg":avg, "rank":rank}
    students.append(s)
    stuNo += 1
    print(f"{name} 학생성적이 저장되었습니다.")
    print("♥")
    print(students)

choice = input("원하는 번호를 입력하세요. >> ")

if choice == "1":
  stu_input()

  