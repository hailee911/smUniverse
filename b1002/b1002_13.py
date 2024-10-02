import random
aArr = []

# 0-9 랜덤숫자를 추출해서 10번 추가하시오 
# 같은 숫자가 있으면 제외하고 입력
# for i in range(10):
#   r_num = random.randint(0,9)
#   if r_num not in aArr:
#     aArr.append(r_num)

i = 0
while(i < 10): # 10개 일 때 종료
  r_num = random.randint(0,9)
  if r_num not in aArr:
    aArr.append(r_num)
    i += 1
    
  

print(aArr)
