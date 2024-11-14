# 클래스 생성
class Car:

  def __init__(self,color,tire,gear,speed):

    self.color = color
    self.speed = speed
    self.tire = tire
    self.gear = gear

  def upSpeed(self,value):
    if value > 0: self.speed += value
    else: 
      ("값을 잘못 넣었습니다.")
    
  def downSpeed(self,value):
    self.speed -= value

# 클래스 사용하려면 클래스 선언 !! 해야 함
c1 = Car("흰색",4,"auto",0)
c1.color = '블루'
c1.speed = 300
print(c1.color)



# 속도 = 0 -> 100


# 리스트,딕셔너리 변수 직접 값을 할당하는 방식 

# speed 변수에 직접 값을 할당
# c1.speed = 100
# print(c1.speed)

# c1.upSpeed(-100)
# print(c1.speed)

# c2 = Car()
# c2.color = "빨강"
# print(c2.color)
# print(c1.color)

