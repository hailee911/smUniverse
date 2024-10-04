import random

# 랜덤숫자 : 1-100
random.randint(1,100)

# 10번 도전에서 입력한 숫자가 더 크면 작은수를 입력하셔야 합니다.
# 입력한 숫자가 더 작으면 큰수를 입력하셔야 합니다.
# 10번 도전에서 맞추지 못하면 , 10번 도전에 실패했습니다. 랜덤숫자 : n
# 도전에 성공했습니다. 랜덤숫자 : n

num = random.randint(1, 100)
cnt = 0

for i in range(10):
  print(i+1,"번째 시도")
  a = int(input("숫자를 입력하세요 : "))
  if a > num:
    print("작은수를 입력하셔야 합니다.")
  elif a < num:
    print("큰수를 입력하셔야 합니다.")
  else:
    print("도전에 성공했습니다. 랜덤숫자 :", num)
    cnt = 1
    break
  
if cnt == 0:
  print("10번 도전에 실패했습니다. 랜덤숫자 : ", num)

