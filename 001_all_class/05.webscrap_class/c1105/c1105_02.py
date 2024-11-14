# # 함수선언
# def func(n1,n2):
#   print(n1)
#   print(n2)

# # 함수호출
# func(10,20)

# 함수선언 가변매개변수
def func(*num):
  print(num) # 튜플타입
  print(len(num))
# 함수호출
func(10)
func(10,20)
func(10,20,30)