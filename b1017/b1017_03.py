
# f = open('b1017/a.txt','w',encoding='utf-8')
# try:
#   f.write("안녕하세요.1\n")
#   f.write("안녕하세요.2\n")
#   f.write({"a":1})
#   f.write("안녕하세요.1")
# except Exception as e:
#   print(e)
# finally:
#   f.close()
# # try-except
# # try - except - else
# # try - except - finally

# print("파일 open")
# try:
#   print("글쓰기 1")
#   print("글쓰기 2")
#   print("글쓰기 3")
#   print("str -> 딕셔너리 입력 ") # 에러
#   print("글쓰기 5")
#   print("글쓰기 6")
#   # print("파일 close")
# except:
#   print("잘못된 타입이 들어왔습니다.")
#   # print("파일 close")
# finally:
#   print("파일 close")

# print("프로그램을 종료합니다.")


# print("1")
# try: # try 구분에 에러가 발생해야 except 실행시킴
#   print("2")
#   # print(3/0)
#   print("3")
#   print("4")
# except:
#   print("5")
#   print("6")
# else:
#   print('프로그램 에러가 발생하지 않으면 실행')
# finally:
#   print('무조건')


# # list_a = [1,2,3,4,5,"홍길동",6,7]
# # list_b = []
# # # 숫자에 **2를하는 프로그램을 구현하시오.
# # try:
# #   for a in list_a:
# #     list_b.append(a**2)
# # except Exception as e:
# #   print(e)

# # print(list_b)

# # n_str = input("반지름 입력하세요.>> ")
# # try:
# #   num = int(n_str)
# #   # 원 넓이, 둘레
# #   print("원 넓이 : ", (num**2)*3.14)
# #   print("원 둘레 : ", 2*num*3.14)
# # except Exception as e:
# #   print("정수가 아닙니다. 정수를 입력하세요.",e)
# # if n_str.isdigit():
# #   num = int(n_str)

# #   # 원 넓이, 둘레
# #   print("원 넓이 : ", (num**2)*3.14)
# #   print("원 둘레 : ", 2*num*3.14)
# # else:
# #   print("정수가 아닙니다. 정수를 입력하세요.")

# # 예외처리 : try-except 구문을 사용해서 처리
# # print("프로그램 시작")
# # try:
# #   print("프로그램 시작")

# # except:
# #   print("에러가 발생 되었습니다.")

# # print('프로그램 종료')