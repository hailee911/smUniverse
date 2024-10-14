# 두수를 입력받아 더하기를 출력하시오.
def plus():
  n1 = int(input("숫자 입력 >> "))
  n2 = int(input("숫자 입력 >> "))
  print("결과: ",n1+n2)

plus()



# def plus(n1,n2):
#   result = n1+n2
#   return result

# print(plus(1,2))
# print(plus(55,45))
# print(plus(50,50))



# # 2,50 합 3,7 합 5,50 합을 모두 더해서 출력하시오.
# def sum(st, ed):
#   sum = 0
#   for i in range(st, ed):
#     sum += i
#   return sum

# a = sum(2,50)
# b = sum(3,7)
# c = sum(5,50)

# print("총합 : ",a+b+c)
# print(f"2-50까지의 합 : {sum(2,50):,d}") # 1,224


# # def num_sum(st, end):
# #   sum = 0
# #   for i in range(st, end):
# #     sum += i
# #   return sum


# # total = 0
# # num_sum(1, 10)
# # num_sum(1, 100)
# # total = num_sum(1, 10) + num_sum(1, 100)
# # # 1,10까지의 합과 1,100까지의 합의 총합을 출력하시오.
# # print("합계 : ", total)

# # print("프로그램 종료")


# # def num_sum(st,end): #(매개변수, 매개변수)
# #   sum = 0
# #   for i in range(st,end+1):
# #     sum += i
# #     print("합계 : ",sum)

# # # num_sum(1,100)

# # # 두수를 입력받아, 그 사이의 숫자 합을 구하시오
# # # num1, num2
# # num1 = int(input("숫자 입력 >> "))
# # num2 = int(input("숫자2 입력 >> "))

# # num_sum(num1,num2)