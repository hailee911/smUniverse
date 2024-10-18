class Circle:
  def __init__(self,length):
    self.__length = length # 변수 직접적으로 접근 제한

  def get_area(self):
    return 3.14 * (self.__length**2)
  def get_dulrae(self):
    return 3.14 * 2 * self.__length

c1 = Circle(int(input("반지름 입력>> ")))
print("넓이 : ",c1.get_area())
print("둘레 : ",c1.get_dulrae())

c2 = Circle(int(input("반지름 입력>> ")))
print("넓이 : ",c2.get_area())
print("둘레 : ",c2.get_dulrae())

# 절차적인 형태의 프로그램 구현
# 반지름을 입력받아 원의 둘레와 넓이를 출력하시오

# r = int(input("반지름 입력>> "))
# print("원의 둘레 : ",3.14*r*2)
# print("원의 넓이 : ",3.14*(r**2))