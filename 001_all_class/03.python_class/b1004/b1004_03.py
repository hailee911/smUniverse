# 0 부터 1씩 증가하면서, 10번 실행
for i in range(10):
  print(i)

print("-"*50)

# 5부터 9 (10이전)까지 5번 실행
for j in range(5, 10):
  print(j)

print("-"*50)

a_list = [1,2,3,4,5]
for k in a_list:
  print(k)

print("-"*50)

b_list = [3,5,9,10,20]
for m in b_list:
  print(m)

print("-"*50)

# 딕셔너리 타입 - {} : json타입과 모양이 같음. 키, 값 (key, value)
dic = {
  "번호" : 1,
  "이름" : "홍길동",
  "국어" : 100,
  "영어" : 100,
  "수학" : 99
}
# print(dic["번호"])
# print(dic["이름"])

for n in dic: # dic에서 key값을 n에 넣어줌.
  # print(n)        # key값이 출력이 됨.
  print(dic[n])   #key값의 value값이 출려이 됨

print("-"*50)

# 리스트 길이 : len()
print(len(b_list))

# 리스트 안에 해당되는 숫자가 몇개인지 확인 - count
print(b_list.count(5))

# 리스트 추가 - append, insert, extend([2,3]) 
# 리스트 삭제 - del, remove, clear - 모두삭제
