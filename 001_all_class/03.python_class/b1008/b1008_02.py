# [0,3,6,9,12...57]
aArr = []
for i in range(20):
  aArr.append(3*i)
print(aArr)

# [4,5] 2차원 리스트 (헷갈림)
a_list = []
for i in range(4):
  a = []
  for j in range(5):
    a.append(aArr[5*i+j])
  a_list.append(a)

print(a_list)



# # 4행 5열의 2차원 리스트를 만들고, 0부터 3의 배수를 입력하고 출력하세요.
# # 0 3 6 9 12
# # 15 18 21 24 27
# # 30 33 36 39 42
# # 45 48 51 54 57

# a_list = []

# for i in range(4):
#   a = []
#   for j in range(5):
#     a.append(5*3*i+(3*j))
#   a_list.append(a)

# # print(a_list)

# # for l in a_list:
# #   for m in l:
# #     print(m, end="\t")
# #   print()

# for i in range(4):
#   for j in range(5):
#     print(a_list[i][j], end="\t")
#   print()