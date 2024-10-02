# 문자열

# 문자열숫자
a = "123"
print(type(a))          # str
print(type(int(a)))     # int

b = "12.3"
# print(type(int(b)))     # error - 소수점이 있는 문자열 숫자는 float 변경
print(type(float(b)))     # float

c = 12.3
print(type(int(c)))
print(int(c))     # 12

# 문자열 연결 연산자
s1, s2 = "안녕", "안녕하세요"
print(s1+s2)      # 안녕안녕하세요

# 문자열 반복 연산
print("안녕" * 10)
print("-"*30)

# 문자열 슬라이싱
str1 = "안녕하세요.반갑습니다."     # 문자열자체 - 리스트 형태
print(str1[0])      # 안
print(str1[6])      # 반
print(str1[2:5])    # 해당범위출력 : [위치:위치한칸뒤]
print(str1[:5])     # [처음:숫자 앞까지]
print(str1[1:10:2]) # [위치:숫자 앞까지: step 2]
print(str1[::-1])   # 처음부터 끝까지 로꾸꺼(-1)

# [] - 배열 : 배열은 한번 범위가 정해지면 수정 불가능 : c, 자바
# [] - 리스트 : 범위 상관 없음 : 파이썬


# input_str = input("글자를 입력하세요.")

# # 문자가 입력되지 않았을 때,

# if input_str == "":
#   print("글자를 입력하셔야 합니다.")
# else:
#   print("입력문자 : ",input_str)
#   print("프로그램이 종료됩니다.")

