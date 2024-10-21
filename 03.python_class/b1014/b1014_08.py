# num = int(input("숫자를 입력하세요.>> "))
# num2 = int(input("숫자를 입력하세요.>> "))

# def calc(num,num2):
#   print(f"두수 더하기 : {num+num2}")
#   print(f"두수 빼기 : {num-num2}")
#   print(f"두수 곱하기 : {num*num2}")
#   print(f"두수 나누기 : {num/num2}")
#   print("-"*30)

# numStr = input("숫자를 입력하세요. (12,5)")
# num = numStr.split(",")
# n1 = int(num[0])
# n2 = int(num[1])
# print(type(n1))
# calc(n1,n2)

# # 3개의 숫자를 입력받아 숫자를 계산하시오. 12,5,3
# a = int(input("숫자1 >> "))
# b = int(input("숫자2 >> "))
# c = int(input("숫자3 >> "))

# def three(a,b,c):
#   print(f"두수 더하기 : {a+b+c}")
#   print(f"두수 빼기 : {a-b-c}")
#   print(f"두수 곱하기 : {a*b*c}")
#   print(f"두수 나누기 : {a/b/c}")
#   print("-"*30)

# three(a,b,c)

# 함수사용
# def calc(num, num2):
#   print(f"두수 더하기 : {num+num2}")
#   print(f"두수 빼기 : {num-num2}")
#   print(f"두수 곱하기 : {num*num2}")
#   print(f"두수 나누기 : {num/num2}")
#   print("-"*30)

# num = [10,20,30]
# num2 = [5,7,3]

# for i in range(len(num)):
#   calc(num[i],num2[i])

# for문을 활용한 계산
# num = [10,20,30]
# num2 = [5,7,3]

# for i in range(len(num)):
#   print(f"두수 더하기 : {num[i]+num2[i]}")
#   print(f"두수 빼기 : {num[i]-num2[i]}")
#   print(f"두수 곱하기 : {num[i]*num2[i]}")
#   print(f"두수 나누기 : {num[i]/num2[i]}")
#   print("-"*30)



# num = 20
# num2 = 7

# print(f"두수 더하기 : {num+num2}")
# print(f"두수 빼기 : {num-num2}")
# print(f"두수 곱하기 : {num*num2}")
# print(f"두수 나누기 : {num/num2}")


# 배열로 함수
# def calc(numStr2):
#   s1 = 0
#   s2 = 0
#   s3 = 1
#   s4 = 1
#   for i in numStr2:
#     s1 += i
#     s2 -= i
#     s3 *= i
#     s4 /= i
#   print(f"배열 더하기 : {s1}")
#   print(f"배열 빼기 : {s2}")
#   print(f"배열 곱하기 : {s3}")
#   print(f"배열 나누기 : {s4}")

# numStr = input("숫자를 입력하세요. (12,5,3)")
# numStr2 = numStr.split(",")
# numStr2 =[int(i) for i in numStr2 ] #리스트 내포
# print(numStr2)

# calc(numStr2)

# 가변 매개변수 *n
# def calc(*n):
#   print(n)

# calc(1,2,3)

# 키워드 매개변수 calc() -> 10 calc(20) -> 20
# def calc(n1 = 10, n2 = 20):
#   print(n1)
#   print(n2)


# calc() # 매개 변수가 없으면 기본 값으로 출력
# calc(30) # n1 -> 30 n2 -> 20
# calc(300) # 키가 없으면 무조건 1번째로 전달이 됨.
# calc(n2 = 100) # 키가 있으면 키 값으로 전달이 됨.

# 가변 매개변수
# print(1,2,3,sep=",",end="\t")
# print('안녕')

# 함수 내에 선언된 변수는 외부에서 사용할 수 없음.
# def calc(v1,v2):
#   global sum  # 전역변수 global
#   # sum = 0   # 지역변수
#   for i in range(v1,v2+1):
#     sum += i
#   return sum
# sum = 100 # 외부의 변수를 사용해서 계산을 하고 싶을 경우
# sum = calc(1,10)


# def calc(n1,n2):
#   s1 = n1+n2
#   s2 = n1-n2
#   s3 = n1*n2
#   s4 = n1/n2
#   return s1,s2,s3,s4

# s5 = calc(10,5)
# print(s5)

# 매개변수가 일반변수 일경우 return 하지 않으면 변수값이 변동이 없음.
# hh = 100

# def add(hh):
#   hh = hh + 100

# add(hh)
# print(hh)

# ------------------------------------------------------------------------------

# 복합변수 - 리스트, 딕셔너리
# hong = [1,2,3,4,5]

# # # # 매개변수가 복합변수 일 경우 return 없어도 값이 변경되어 전달 됨. # # #
# def add(h):
#   for i in range(len(h)):
#     h[i] = h[i]+100

# add(hong)
# print(hong)


# 전역변수인 경우 함수 내에서도 사용이 가능하고
# 함수 외부에서도 사용이 가능함.
def calc():
  global sum # 전역변수인 경우, 함수에서 변경시 외부에서도 같이 변경이 됨.
  sum = 200

sum = 10
calc() # 함수에서 sum을 200으로 변경이 됨.
print(sum) # 결과값은 sum이 200됨.
