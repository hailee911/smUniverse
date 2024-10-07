import random

# 1-25까지 랜덤의 숫자 25개를 중복 없이 추출해서
# [5,5] 2차원 리스트에 입력해서 출력하시오.

# a_list = []
# b_list = []
# while len(a_list) < 25:
#   num = random.randint(1,25)
#   if num not in a_list:
#     a_list.append(num)

# for i in range(0, len(a_list),5):
#   b_list.append(a_list[i:i+5])


# print(a_list)
# print(b_list)

a_list = list(range(1, 26))
random.shuffle(a_list)

b_list = []

for i in range(0, len(a_list), 5):
    b_list.append(a_list[i:i + 5])  # 5개씩 잘라서 추가

# 결과 출력
for row in b_list:
    print(row)

while True:
    print("\t0\t1\t2\t3\t4")
    print("-"*50)
    for i in range(5):
        print(i,end="\t")
        for j in range(5):
            print(b_list[i][j],end="\t")
        print()
    input1 = input("좌표를 입력하세요. [0,1] >> ")
    print()
    input2 = input1.split(",")
    print(f"{input1} 좌표의 값 : ", b_list[int(input2[0])][int(input2[1])])