b_list = []
for i in range(5):
  a = []
  for j in range(5):
    a.append((i*5)+j+1)
  b_list.append(a)

print(b_list)



# a_list = [] # a_list[0] - 0항 1항 2항 ... 8번항
# for i in range(9):
#   a_list.append(i+1)

# print(a_list)

# b_list = []
# for i in range(9):    
#   b = []
#   if(i%3) == 0:


# a_list = [
#   [1,2,3,4],
#   [5,6,7,8],
#   [9,10,11,12]
# ]

# # 2차원 리스트 -> for문을 2번 사용
# for i in a_list:
#   for j in i:
#     print(j)

# 1-9 까지 for문을 사용해서 2차원 리스트에 추가하시오
# b_list = []

# for i in range(3):
#   a = []
#   for j in range(3):
#     a.append((i*3)+j+1)
#   b_list.append(a)
    
# print(b_list)
# [[1,2,3],[4,5,6],[7,8,9]]