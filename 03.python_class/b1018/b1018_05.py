class Circle:
  def __init__(self,length):
    self.__length = length # 내부클래스만 변수에 접근해서 수정이 가능

  def get_length(self):
    return self.__length
  
  def set_length(self,length):
    self.__length = length

# 클래스 선언
# _, __ 내부적으로 캡슐화 하겠다고 선언
c1 = Circle(10) # 1. 선언 - 값을 입력
print("c1 길이 : ",c1.get_length()) # 2. getter를 값출력
c1.set_length(200) # 3. setter 값을 입력
print("c1 길이 변경 : ",c1.get_length()) # 4.getter 값출력
c1.__length = 100 # 5. 변수 직접입력
print("직접 변경(100) : ",c1.__length) # 6. 변수 직접출력
print("get 읽어온 length : ",c1.get_length()) # 7. getter 값출력