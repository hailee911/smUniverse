students = [
  {"no": 1, "name": "홍길동", "kor": 100, "eng": 100, "math": 100, "total": 300, "avg": 100.0, "rank": 0},
  {"no": 2, "name": "유관순", "kor": 80, "eng": 80, "math": 85, "total": 245, "avg": 81.67, "rank": 0},
  {"no": 3, "name": "이순신", "kor": 90, "eng": 90, "math": 91, "total": 271, "avg": 90.33, "rank": 0},
  {"no": 4, "name": "강감찬", "kor": 60, "eng": 65, "math": 67, "total": 192, "avg": 64.00, "rank": 0},
  {"no": 5, "name": "김구", "kor": 100, "eng": 100, "math": 84, "total": 284, "avg": 94.67, "rank": 0}
]

print(students)
print("-"*50)
# students.sort(key=lambda x:x['name'], reverse=True) # 딕셔너리 sort
students.sort(key=lambda x:x['total'], reverse=True) # 딕셔너리 sort

# sort - 리스트에서만 지원되는 정렬함수
# 함수  
# def stu_sort(x):
#   return x[1]
# students.sort(key=stu_sort) # 함수를 사용해서 정렬


# 람다식
# 합계순 순차 & 역순 정렬
# students.sort(key=lambda x:x[5])
# students.sort(key=lambda x:-x[5])

# 이름 순 순차 & 역순 정렬
# students.sort(key=lambda x:x[1])
# students.sort(key=lambda x:x[1], reverse=True)

# aArr = [4,5,6,1,2]
# print(aArr)
# aArr.sort() # 순차정렬
# aArr.sort(reverse=True) # 역순정렬
# aArr.reverse() # 거꾸로 출력
# print(aArr)

print(students)