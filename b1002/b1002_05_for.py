students = [
  [1, '이다영', 100,90,99],
  [2, '최민기', 100,100,99],
  [3, '이석민', 100,100,99]
]
print(len(students))

# 반복문
for i in range(3):
  print(students[i])

for i in range(2,5): # 2 부터 5 이전까지 반복 2, 3, 4
  print(i)

for i in range(1,10,2): # 2씩 뛰어서 1,3,5,7,9 1부터 9까지
  print(i)

aArr = [1,2,5,7,8]
for i in aArr: # list의 값을 1개씩 가져와서 출력
  print(i)

for i,data in enumerate(aArr): # list의 값과 index 번호를 함께 출력
  print(i,":",data)


aStr = "안녕하세요"
for i in aStr: # 문자열 list 한글자씩 추출
  print(i)

# enumerate index 번호를 추가해서 가져올 수 있음.
for idx, data in enumerate(aStr):
  print(idx,":", data)


# # 번호,이름,국어,영어,수학
# s = [4, '김민규', 100,90,99]
# # s 리스트에 합계와 평균을 추가하시오.
# print(s)
# s.append(s[2]+s[3]+s[4])
# s.append(round(((s[2]+s[3]+s[4])/3),2))
# print(s)



# 리스트 추가 - append - 뒤에추가 insert - 원하는 위치추가 
# 삭제 : del - 위치삭제, remove - 값으로 검색해서 삭제
# a_list = [1,2,3]
# # 10추가
# a_list.append(10) # 마지막 index에 10 추가
# print(a_list)
# a_list.insert(2, 100) # index 2번에 100 추가
# print(a_list)

# del a_list[2] # index 2번 자리 값 삭제
# print(a_list)
# a_list.remove(10) # 값으로 삭제
# print(a_list)


# 문자열 슬라이싱
# str = "좋은 하루되세요. 많은 행복받으세요. 많은 감사! 많은 돈."
# print(len(str))

# # 뒤쪽에서 5자리 전까지 출력
# print(str[-5:])
# print(str[-1])
# print(str[::-1])