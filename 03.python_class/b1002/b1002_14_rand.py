import random

# 1-100 랜덤숫자 생성
# 입력한 숫자가 랜덤 숫자보다 크면 입력한 숫자가 큽니다.
# 입력한 숫자가 랜덤숫자보다 작으면 입력한 숫자가 작다.
# 10번 도전하도록 하시오.

i = 0
num = random.randint(1, 100)

### while 문 ###

# while i < 11:
#   n = int(input("숫자를 입력하세요. "))
#   if n > num:
#     print("입력한 숫자가 더 큽니다.")
#     i += 1
#   elif n < num:
#     print("입력한 숫자가 더 작습니다.")
#     i += 1
#   else:
#     print("정답입니다!", num)
#     break
#   if i == 11:
#     print("실패했습니다.")

### for 문 ###

count = 0

for i in range(10):
  n = int(input("숫자를 입력하세요. "))
  if n > num:
    print("입력한 숫자가 더 큽니다.")

  elif n < num:
    print("입력한 숫자가 더 작습니다.")
    
  else:
    print("정답입니다!", num)
    count = 1
    break
  
if count == 0:
  print("10번 도전 실패!")
