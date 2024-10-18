# 클래스 생성
# 변수 3종류 (인스턴스 변수)
# 함수 2종료 (인스턴스, 클래스)
# @classmethod # 클래스 함수 표시

class Student:
  no = 0
  kor = 100 # 클래스변수 클래스명.변수명
  def __init__(self,no,name,kor,eng,math):
    self.no += no # 인스턴스 변수 : 참조변수명.변수명
    self.name = name
    self.kor = kor
    self.eng = eng
    self.math = math
    self.total = kor+eng+math
    self.avg = round((kor+eng+math)/3, 2)
    self.rank = 0

  def total(self):
    return self.kor+self.eng+self.math

  def __str__(self): # 문자열
    return f'{self.no}\t{self.name}\t{self.kor}\t{self.eng}\t{self.math}\t{self.total}\t{self.avg}\t{self.rank}'

s1 = Student()

# 1. 학생성적입력
# 이름 국어 영어 수학 -> 번호 국어 영어 수학 합계 평균 등수
# 클래스 1개가 생성이 되고
# 클래스 참조변수(__str__) 출력을 해보세요.

while True:
  choice = int(input("번호 선택 >> "))
  stu = []
  if choice == 1:
    print("[ 학생 성적 입력 ]")
    name = input("이름 입력 >> ")
    kor = int(input("국어 성적 입력 >> "))
    eng = int(input("영어 성적 입력 >> "))
    math = int(input("수학 성적 입력 >> "))
    s = Student(name,kor,eng,math)
    print(s)

