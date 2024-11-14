# 함수 - 매개변수 (일반변수, 복합변수)
# 1. 함수 일반 매개변수 - return이 아니면 값이 함수 밖으로 나올 수 없음


# 2. 전역변수 - 일반매개변수 retrun 없이 함수밖 값 사용

# def calc():
#   global h
#   h += 100

# h = 20
# calc() # 함수 호출 후 h에 값을 할당할 필요 없음.
# print(h)

# def calc():
#   h += 100
#   return h

# h = 20
# # calc(h) # 호출만 하면 값이 변경되지 않음
# print(calc())

# 3. 함수 복합매개변수 - return 없이 함수 밖 값 사용
# def calc(hArr):
#   for i in range(len(hArr)):
#     hArr[i] += 100

# hArr = [1,2,3,4,5] # 복합 변수 - 주소값이 저장됨.
# calc(hArr)
# print(hArr)

def calc():
  print(a)

a = 10 # 전역변수 출력은 가능하지만 함수 내 값 변경은 불가능.
calc()
