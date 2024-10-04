# for 문을 출력
for k in range(1,10):
  print(f"[ {k} 단 ]",end="\t")
print()

for i in range(2,10):
  for j in range(1,10):
    print(f"{j} x {i} = {i*j}", end="\t")
  print()




# 000
# 001
# ...
# 999

# for i in range(0,10):
#   for j in range(0,10):
#     for k in range(0,10):
#       print(i,j,k)

# for i in range(1000):
#   # print("{:03d}".format(i)) #같은 방법
#   print(f"{i:03d}")
  



# # 구구단 ; 입력한 단을 출력하시오.
# a = int(input("단을 입력하세요: "))

# for i in range(a, a+1):
#   for j in range(1,10):
#     print((f"{i} x {j} = {a*j}"))