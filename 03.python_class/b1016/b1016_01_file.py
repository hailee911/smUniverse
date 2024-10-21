# 파일 with
# close() 하지 않아도 됨.
with open('b1016/aa.txt','a', encoding='utf-8') as f:
  f.write("안녕하신가.")


# # 파일 쓰기 - a
# while True:
#   print("[ 메모장 ]")
#   data = input("저장하려는 글자를 입력하세요.>> ")
#   f = open('b1016/aa.txt','a', encoding='utf-8')
#   f.write(data+'\n')
#   f.close()
#   print("글쓰기 종료")





# # 파일 쓰기 - w
# while True:
#   print("[ 메모장 ]")
#   data = input("저장하려는 글자를 입력하세요.>> ")
#   f = open('b1016/aa.txt','w', encoding='utf-8')
#   f.write(data)
#   f.close()
#   print("글쓰기 종료")

# f = open('b1016/aa.txt','w', encoding='utf-8')
# for i in range(1,11):
#   data = f"안녕하세요. {i} \n"
#   f.write(data)
# f.close()
# print("글쓰기 종료")

# f = open('b1016/aa.txt','w', encoding='utf-8')
# f.write("파일쓰기\n")
# f.write("hello world!")
# f.close()
# print("글쓰기 종료")





# 파일 읽기 - r

# # 3. read()
# f = open('b1016/b.txt','r', encoding='utf-8')
# print(type(f)) # <class '_io.TextIOWrapper'>
# # for line in f:
# #   print(line.strip())
# f.close

# # 2. readlines() - 모든 글을 읽어오기
# f = open('b1016/b.txt','r', encoding='utf-8')
# lines = f.readlines()
# print(type(lines)) # list type
# print(lines) # ['파이썬 수업\n', '텍스트 파일 읽어오기']
# for line in lines:
#   print(line.strip())
# f.close

# # 1. readline() - 1줄씩 읽어오기
# # 절대경로를 사용
# f = open('b1016/b.txt','r', encoding='utf-8')
# # f = open('C:/aaa/a.txt','r', encoding='UTF-8')
# while True:
#   line = f.readline()
#   if not line: break
#   print(line.strip()) # \n 값을 생략
# f.close