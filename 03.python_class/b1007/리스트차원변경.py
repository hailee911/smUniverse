# a = [1,2,3,4,5,6,7,8,9]
# b = []

# for i in range(9):
#   print(3*(i//3)+(i%3)) ???

# 1차원 리스트
a_list = []
for i in range(25):
  a_list.append(i)
print(a_list)

# 1차원 -> 2차원 리스트
b_list = []
for i in range(0, len(a_list),5):
  b_list.append(a_list[i:i+5]) # 5개씩 리스트에 넣기

print(b_list)