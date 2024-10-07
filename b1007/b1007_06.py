import random

# 25개 1차원 리스트

# 25개 중 1을 5개 나머지는 0으로 입력해서 출력하시오.
a_list = [0]*20+[1]*5
random.shuffle(a_list)
# print(a_list)
  
b_list = []
for i in range(0, len(a_list), 5):
  b_list.append(a_list[i:i+5])

# print(b_list)

# while True:
#     print("\t0\t1\t2\t3\t4") # 표의 x축
#     print("-"*50)
#     for i in range(5):
#         print(i,end="\t") # 표의 y축
#         for j in range(5):
#             print(b_list[i][j],end="\t")
#         print()
#     input1 = input("좌표를 입력하세요. [0,1] >> ")
#     print()
#     input2 = input1.split(",")
#     print(f"{input1} 좌표의 값 : ", b_list[int(input2[0])][int(input2[1])])
#     break

# 2차원 배열로 표시
for i in range(5):
  print(i,end="\t")
  for j in range(5):
    print(b_list[i][j],end="\t")
  print()