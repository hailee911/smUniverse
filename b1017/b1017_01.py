# a = 10 # 전역변수
# b = 20
# c = 30
# sum = 0

# def add(a,b,c):
#   return a+b+c
# a = add(a,b,c)
# print(a)


# 함수선언
# def func(a):
#   # global a
#   print(a)
#   a += 50
#   return a

# # 함수호출
# a = func(a)
# print(a)

subject = ['국어','영어','수학']
score = []
while True:
  print("[ 1. 과목 추가 ]")
  print("[ 0. 종료 ]")
  print("-"*20)
  choice = input("원하는 번호를 입력하세요.>>")
  if choice == "1":
    s_input = input("과목을 추가하세요.>> ")
    subject.append(s_input)
  elif choice == "0":
    break
  
sum = 0
for i in range(len(subject)):
  score.append(int(input(f"{subject[i]}점수를 입력하세요.>> ")))
  sum += score[i]

print(dict(zip(subject,score)),"총합: ",sum)



# num1 = int(input("국어 점수를 입력하세요.>> "))
# num2 = int(input("영어 점수를 입력하세요.>> "))
# num3 = int(input("수학 점수를 입력하세요.>> "))
# num4 = int(input("과학 점수를 입력하세요.>> "))

# print("국어: ",num1)
# print("영어: ",num2)
# print("수학: ",num3)
# print("과학: ",num4)
# print("합계: ",(num1+num2+num3+num4))



# def output(subject):
#    # 출력
#   print("과목")
#   print("-"*20)
#   for s in subject:
#     print(s)  

# while True:
#   print("[ 과목 생성 프로그램 ]")
#   s_input = input("원하는 과목을 입력하세요.>> ")
#   subject.append(s_input)
#   output(subject)

