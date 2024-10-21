import random
# 숫자 맞추기 게임
# 입력된 숫자 리스트에 저장해 출력

a_list = []
count = 0
num = random.randint(1, 100)

for i in range(10):
  a = int(input("숫자를 입력하세요. >> "))
  a_list.append(a)
  if a < num:
    print("더 큰 숫자를 입력하세요.")
    print()
  elif a > num:
    print("더 작은숫자를 입력하세요.")
    print()
  else:
    print("정답입니다! 정답: ",num)
    count = 1
    break

if count == 0:
  print("10번 도전 실패! 정답: ",num)

print("입력된 숫자 :", a_list)

