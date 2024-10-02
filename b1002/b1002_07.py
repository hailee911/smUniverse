students = [
  [1, '이다영', 100,90,99],
  [2, '최민기', 100,100,99],
  [3, '이석민', 100,100,99],
  [4, '권순영', 100,90,99],
  [4, '전원우', 100,90,99]
]

# 이름을 입력받아 같은 이름이 있으면 데이터 삭제 없으면 없습니다. 출력
name = input("이름을 입력하세요. :")
for s in students:
  if name == s[1]:
    students.remove(s)
    print(students) 
  else:
    print("없는 이름입니다.")

    
  



# a = [1, '홍길동', 100]
# b = [2, '유관순', 200]
# c = [3, '이순신', 100]
# all_list = [a,b,c]
# d = [3, '이순신', 100]

# # 데이터값으로 삭제 - remove
# all_list.remove(d)
# print(all_list)

# # 이름이 유관순인것을 삭제하시오.
# for i in all_list:
#   if i[1] == '유관순':
#     all_list.remove(i)
#     print(all_list)



# aArr = [2,3,4,6,7,8,9,10]

# print(aArr)
# # 50, 100 추가
# aArr.append(50)
# aArr.append(100)
# print(aArr)

# # 2번자리에 30 추가
# aArr.insert(2, 30)
# print(aArr)

# # 숫자 6 삭제
# aArr.remove(6)
# print(aArr)

# # index 0, 3 데이터 삭제
# del aArr[0]
# del aArr[3]
# print(aArr)