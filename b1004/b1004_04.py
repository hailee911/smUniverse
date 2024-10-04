# 두 수를 입력받아, 두수까지 합계를 구하시오 
# 예) 3,8 -> 3+4+5+6+7+8

a = int(input("숫자를 입력하세요 : "))
b = int(input("숫자를 입력하세요 : "))
sum = 0

# 1. min, max 함수 사용

# for i in range(min(a,b), max(a,b)+1):
#   sum += i
# print("합계: ",sum)

# 2. if 사용

# max_num = 0
# min_num = 0

# if a>b:
#   max_num = a
#   min_num = b

#   for i in range(min_num, max_num+1):
#     sum += i
#   print("합계: ",sum)

# 3. if 다른 방법 파이썬만 가능 - 두개 변수 치환

# if a>b:
#   a,b = b,a

# for i in range(a, b+1):
#   sum += i
# print("합계: ",sum)

# -----------------------------------------------------

# 1 3 5 7 9 ... 99 합계를 구하시오
# sum = 0
# for i in range(1,101,2):
#   sum += i
# print("합계 : ", sum)



# 1,100까지 숫자의 합
# sum = 0
# for i in range(1,101):
#   sum += i
#   print("합계 : ",sum)




# for _ in range(3):
#   print("안녕하세요")


# for문 리스트
# for i in [1,2,3]:
#   for j in range(i):
#     print("안녕하세요 "*i)
#   print("-"*20)

# for i in [1,2,3]:
#   print("안녕하세요 \n"*i)





# 역순 5 -> 1 -1씩 감소
# for i in range(5,0,-1):
#   print("*"*i)


# for문을 사용해서
# for i in range(0,6):
#   print("*"*i)



# # 1, 3, 5, 7, 9 구구단
# for i in range(1,10):
#   if i%2 != 0:
#     print(f"[ {i} 단 ]")
#     for j in range(1,10):
#       print(f"{i} x {j} = {i*j}")
#     print("-"*20)

# # 1, 3, 5, 7, 9 구구단 >> 다른 방법
# for i in range(1, 10, 2): #(시작값, 끝값+1, 증가값)
#   print(f"[ {i} 단 ]")
#   for j in range(1,10):
#     print(f"{i} x {j} = {i*j}")
#   print("-"*20)

# 구구단을 출력하시오.
# for i in range(2,10):
#   print(f"[ {i} 단 ]")
#   for j in range(1,10):
#     print(f"{i} x {j} = {i*j}")
#   print("-" * 20)



# 1,3,5,7,9까지 출력하시오.
# for i in range(10):
#   if i%2 != 0:
#     print(i)



# 1, 10까지 for문을 사용해서 출력하시오.
# for i in range(1,11):
#   print(i)