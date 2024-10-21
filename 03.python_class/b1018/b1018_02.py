# class 생성방법

# 학생1명 정보
# 번호,이름,국어,영어,수학,합계,평균,등수
# 학생클래스 설계도 생성
class Student:
  # 기본 생성자
  # def __init__(self):
  #   None
  # 매개변수가 있는 생성자
  def __init__(self,no,name,kor,eng,math):
    self.no = no
    self.name = name
    self.kor = kor
    self.eng = eng
    self.math = math
    self.total = kor+eng+math
    self.avg = round((kor+eng+math)/3, 2)
    self.rank = 0
  
  def print(self):
    print(f"{self.no}\t{self.name}\t{self.kor}\t{self.eng}\t{self.math}")

# 클래스 사용방법
# 클래스 선언
s1 = Student(1,'이다영',100,100,99)
# print(s1) # 주소값이 출력됨
print(s1.no,s1.name,s1.kor,s1.eng,s1.math,s1.total,s1.avg,s1.rank)
s1.print()

# # 클래스명.변수명 = 값 : 변수가 생성되어 클래스에 변수가 저장됨.
# 기본생성자 사용해서 값을 개별적으로 입력방식
# s1.no = 1
# s1.name = '홍길동'
# s1.kor = 100
# s1.eng = 100
# s1.math = 100

# 클래스내 변수 출력
# print(s1.no)
# print(s1.name)

