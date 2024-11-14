# # name, kor, eng, math, total, avg
# 홍길동 100 100 99

name = input("이름 작성 : ")
n1 = input("국어 점수 : ")
n2 = input("영어 점수 : ")
n3 = input("수학 점수 : ")
tot = int(n1) + int(n2) + int(n3)
avg = tot/3
print("{} 합계 : {}, 평균 : {}".format(name, tot, round(avg, 2)))
# f식 프린트 방법
print(f"{name},{n1},{n2},{n3},{tot},{avg:.2f}")








# a = '100'
# print(type(a))
# b = "200"
# print(type(b))

# print(a+b) # 문자연결연산자 100200
# print(int(a)+int(b)) # 타입 변경 300 

# c = "3.14"
# print(int(float(c))) # 실수형으로 변경 후 정수형으로 변경 3
# # print(int(c)) # 문자 실수형은 정수로 바로 변경 불가
# print(str(c)) # 실수형은 문자열로 변경

# d = "True"
# print(bool(d)) # 문자 불형을 불형으로 변경
# # 타입 변경 - str float int bool



# name = "이다영"
# print(type(name)) #<class 'str'>

# level = '3레벨'
# print(type(level))

# a_bool = True #True False
# print(type(a_bool)) #<class 'bool'>

# var1 = 100
# var2 = var1
# var3 = var2
# var4 = var3
# print(var4)

# v4 = v3 = v2 = v1 = 10
# print(v4)