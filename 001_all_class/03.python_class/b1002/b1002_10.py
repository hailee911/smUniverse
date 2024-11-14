fruit = []

while True:
  # strip() 앞쪽여백, 뒤쪽여백 제거 '사 과' 는 안됨
  # replace(" ", "") 문자 대체 함수
  search = input("과일이름을 입력하세요. (종료: x)").replace(" ","")

  if(search == 'x'):
    break

  if search in fruit:
    print("같은 이름이 있습니다.")
  else:
    print(f"{search}을(를) 추가합니다.")
    fruit.append(search)
    print("모든 과일이름 : ",fruit)      




# 반복문을 종료할 때 : break
# while True:
#   break
# print("프로그램 종료")


# 무한 반복문은 while True 입력
# a = 0
# while True: # 무한반복
#   print(a)
#   a += 1

# while (a<10):
#   a += 1
#   print(a)

# print("프로그램 종료")
