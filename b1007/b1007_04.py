import random

# 1,25 사이의 랜덤숫자를 생성해서 출력하시오.

a_list = []
# 1~25 랜덤 숫자를 입력, 중복은 제거하고 출력을 하시오

# while len(a_list) < 25:
#   num = random.randint(1,25)
#   if num not in a_list:
#     a_list.append(num)
    
  
# print(a_list)
# print(len(a_list))

# 1-25 랜덤으로 배치 - random.sample()
# 0부터 24까지의 숫자를 몇개 랜덤으로 뽑아 리스트에 넣기
a_list = []
for i in range(25):
  a_list.append(i+1)  

# b_list = random.sample(a_list,5) # 범위 내 리스트, 25개 추출(중복 안됨)
# print(b_list)

# random.choice() - 랜덤
# b_list = random.choice(a_list, k=25)