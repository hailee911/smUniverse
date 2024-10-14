stu_title = ['국어','영어','수학','합계']
# print(stu_title[0]) # 국어 0+1 = 1번
students = {"국어": 100, "영어": 100, "수학": 99, "합계": 299}

print("[ 점수 수정 ]")
print("1. 국어")
print("2. 영어")
print("3. 수학")

choice = int(input("수정하려는 과목을 선택하세요. >> "))

# if choice == 1:
#   print("현재 {}점수 : {}".format(stu_title[0], students[stu_title[0]]))
#   students[stu_title[0]] = int(input(f"변경 {stu_title[0]} 점수를 입력 >> "))
# elif choice == 2:
#   print("현재 {}점수 : {}".format(stu_title[1], students[stu_title[1]]))
#   students[stu_title[1]] = int(input(f"변경 {stu_title[1]} 점수를 입력 >> "))
# elif choice == 3:
#   print("현재 {}점수 : {}".format(stu_title[2], students[stu_title[2]]))
#   students[stu_title[2]] = int(input(f"변경 {stu_title[2]} 점수를 입력 >> "))
  
# students['합계'] = students["국어"]+students["수학"]+students["영어"]
# print("변경 : ",students)

def score(choice):
  print("현재 {}점수 : {}".format(stu_title[choice-1], students[stu_title[choice-1]]))
  students[stu_title[choice-1]] = int(input(f"변경 {stu_title[choice-1]} 점수를 입력 >> "))

  students['합계'] = students["국어"]+students["수학"]+students["영어"]
  print("변경 : ",students)

score(choice)

