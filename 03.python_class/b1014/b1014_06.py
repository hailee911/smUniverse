import random

# tName = ["이름","국어","영어","수학","합계"]

# fName = ["문준휘", "귤", "체리", "도겸", "버논", "호랑이"]

fruit = {"문준휘":"jun", "귤":"boo", "체리":"s-coups","도겸":"dk", "버논": "vernon", "호랑이":"hoshi"}

# random.shuffle(fName) # 원본이 변경이 됨.
# fName 랜덤순서로 영문퀴즈 시작
re_fruit = random.sample(list(fruit.keys()), 5)
for i in re_fruit:
  search = input(f"{i}의 영문을 입력하세요. >> ")
  if fruit[i] == search:
    print("정답입니다.", fruit[i], search)
  else:
    print("오답입니다.", fruit[i], search)

# print("[ 영단어 맞추기 ]")
# for key in fruit.keys():
#   search = input(f"{key}의 영문을 입력하세요. >> ")
#   if fruit[key] == search:
#     print("정답입니다.", fruit[key], search)
#   else:
#     print("오답입니다.", fruit[key], search)



# 바나나 입력 시 banana
# print(fruit['호랑이'])
# print(fruit['귤'])

# while True:
#   search = input("과일이름을 입력하세요. >> ")
#   if search not in fruit:
#     print("찾는 과일이 없습니다.")
#   else:
#     print(search,"=",fruit[search])