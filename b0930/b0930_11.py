# 1759870
# 9870
# 590
a = int(input("입력: "))

if a > 50000:
  print("5만원 :", a//50000, "장 필요")
  b = a%50000
  print("남은 돈 :", b)

else:
  print("돈이 부족합니다.")




# str1 = input("문자를 입력하세요.")
# a = len(str1) #문자의 길이
# if a==5:
#   print("a는 5입니다.")
# elif a==4:
#   print("a는 4입니다.")
# elif a==3:
#   print("a는 3입니다.")
# else:
#   print("a 숫자는 2이하입니다.")


# money = 1759870
# # 50000, 10000, 5000, 1000, 500, 100, 50, 10

# a = money // 50000
# b = (money % 50000) // 10000
# c = ((money % 50000)%10000)//5000
# d = (((money % 50000)%10000)%5000)//1000
# e = ((((money % 50000)%10000)%5000)%1000)//500
# f = (((((money % 50000)%10000)%5000)%1000)%500)//100
# g = ((((((money % 50000)%10000)%5000)%1000)%500)%100)//50
# h = (((((((money % 50000)%10000)%5000)%1000)%500)%100)%50)//10

# print(a, b, c, d, e, f, g, h)




# money = 780
# # 500 - 1
# print("500원 동전개수 :",money // 500)
# # 100 - 2
# print("100원 동전개수 :",(money%500)//100)
# # 50 - 1
# print("50 원 동전개수 :", ((money%500)%100)//50)
# # 10 - 3
# print("10 원 동전개수 :", (((money%500)%100)%50)//10)
# print("남은  동전개수 :", (((money%500)%100)%50)%10)
