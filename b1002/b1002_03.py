# if문

num = int(input("숫자를 입력하세요."))


if 98 <= num <= 100 :
  print("A+")
elif 94<= num:
  print("A")
elif 90<= num:
  print("A-")
elif 88<= num:
  print("B+")
elif 84<= num:
  print("B")
elif 80<= num:
  print("B-")

else:
  print("F")