subName = ["국어","영어","수학"]
score = {"국어":100,"영어":95,"수학":80}
# print(score['국어'])
# print(score[subName[0]])

# for i in subName:
#   print(i,":", score[i])

for k,v in score.items():
  print(k,":",v)


### 구구단 출력 ###
# for i in range(2,6):
#   for j in range(1,10):
#     print(f"{i} x {j} = {i*j} \n")

# def gugudan(n):
#   for i in range(2, n+1):
#     print("[ {} 단]".format(i))
#     for j in range(1, 10):
#       print(f"{i} x {j} = {i*j}" )
#     print("\n")

# nArr = [9,5,7]
# # 2-9 2-5 2-7
# for i in nArr:
#   gugudan(i)
#   print("-"*50)

