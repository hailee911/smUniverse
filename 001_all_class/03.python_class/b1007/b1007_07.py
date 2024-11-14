import random

# 로또


a_list = [
  [0,1,0],
  [0,0,1],
  [1,0,0]
]

aa_list = [
  ["로또","로또","로또"],
  ["로또","로또","로또"],
  ["로또","로또","로또"]
]

while True:
  print("\t0\t1\t2")
  for i in range(3):
    print(i, end="\t")
    for j in range(3):
      print(a_list[i][j], end="\t")
    print()

  code = input("좌표 입력 >> ")
  codeArr = code.split(".")
  print("좌표값 : ", a_list[int(codeArr[0])][int(codeArr[1])])

  if a_list[int(codeArr[0])][int(codeArr[1])] == 1:
    print("당첨")
  elif a_list[int(codeArr[0])][int(codeArr[1])] == 0:
    print("꽝")