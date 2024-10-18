s_title = ['번호','이름','국어','영어','수학','합계','평균','등수']
class Student:
  # 인스턴스 변수 - 객체선언을 하면 변수는 개별적으로 생성
  count = 0 # 클래스 변수 - 모든 객체가 동일한 변수를 사용
  students = [] # 클래스 리스트

  # 클래스 함수
  @classmethod
  def stu_print(cls):
    print(*s_title,sep="\t")
    print("-"*80)
    for s in cls.students:
      print(str(s))

  def __init__(self,name,kor,eng,math):
    Student.count += 1
    self.no = Student.count # 클래스변수 - 공용으로 변수를 사용
    self.name = name
    self.kor = kor
    self.eng = eng
    self.math = math
    self.total = kor+eng+math
    self.avg = round((kor+eng+math)/3, 2)
    self.rank = 0
    # 클래스 리스트에 추가
    Student.students.append(self)

  # 객체를 문자열 리턴 함수 - 리턴 : 문자열이 되어야 함
  # 참조 변수를 출력할 때 리턴되는 함수
  def __str__(self):
    return f'{self.no}\t{self.name}\t{self.kor}\t{self.eng}\t{self.math}\t{self.total}\t{self.avg}\t{self.rank}'

  def print(self): # 딕셔너리 타입으로 리턴
    return {'no':self.no,'name':self.name,'kor':self.kor,'eng':self.eng,'math':self.math,'total':self.total,'avg':self.avg,'rank':self.rank}
  

# s1 = Student()
# s1.students
# s2 = Student()
# s2.students

while True:
  print("[ 학생 성적으로 출력 ]")
  print("1. 학생 성적 입력")
  print("2. 학생 성적 출력")
  print("3. 홍길동, 유관순 비교")
  choice = int(input("원하는 번호를 입력하세요."))

  if choice == 1:
    print("[ 학생 성적 입력 ]")
    name = input("이름을 입력하세요. >> ")
    score = []
    for i in range(2,5):
      score.append(int(input(f"{s_title[i]} 점수를 입력하세요. >> ")))
      # students리스트 딕셔너리 타입으로 변경해서 입력 
    Student(name,*score)
    # 클래스 변수 접근 방법
    # for s in Student.students:
    #   print(s)
    # 인스턴스변수 참조변수.변수명
    # 클래스변수 클래스명.변수명, 클래스명.함수명

    # print(s1.students)
    # Student.students.append(Student(name,*score)) # 클래스 저장
  elif choice == 2:
    print("[ 학생성적출력 ]")
    Student.stu_print()
  elif choice == 3: # 홍길동 학생 합계, 유관순 학생 합계 비교
    s1 = Student("홍길동",100,100,90)
    s2 = Student("유관순",90,80,90)




print(s1) # 0x000 -> __str__() 정의 된 형태로 출력
# print(s1.print())
# students.append(s1.print())
# s2 = Student("유관순",100,100,90)
# print(s2.print())
# students.append(s2.print())
# print("-"*50)
# print(students)


# s1 = Student("홍길동",100,100,99)
# print(s1.name)
# print("s1 - ",s1.count) # 1
# s2 = Student("유관순",90,90,99)
# print(s2.name)
# print("s2 - ",s2.count) # 2
# print("s1 - ",s1.count) # 2
