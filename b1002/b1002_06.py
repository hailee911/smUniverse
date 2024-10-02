students = [
  [1, '이다영', 100,90,99],
  [2, '최민기', 100,100,99],
  [3, '이석민', 100,100,99]
]

# ss = [4, '권순영', 100,90,99]
# students.append(ss)

# for i in students: # remove
#   if i[1] == '이석민':
#     students.remove(i)
#     print(students)

for idx, s in enumerate(students): # del
  if  s[1]== '이석민':
    del students[idx]
    print(students)





# print(students) # 한번에 모두 출력

# for s in students: # 1개씩 가져와서 출력
#   print(s)

# 이름이 최민기 인것을 출력하시오.
# for s in students:
#   if s[1] == '최민기':
#       print(s)