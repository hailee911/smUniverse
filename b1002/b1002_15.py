import random

num = random.randint(1,100)
count = 0

for i in range(10):
  i += 1
  print(i, "번째 시도!")
  n = int(input("숫자를 입력하세용 : "))

  if n == num:
    print("정답입니다! 정답: ",num)
    count = 1
    break
  elif n > num:
    print("숫자가 더 큽니다.")
    
  elif n < num:
    print("숫자가 더 작습니다.")
    

if count == 0:
  print("실패했습니다. 정답: ",num)


