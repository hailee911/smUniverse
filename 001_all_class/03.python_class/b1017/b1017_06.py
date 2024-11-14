a = ['20', 'mwathellj', '58', '63', '60', '181', '60', '1']
b = ['20', '58', '63', '60', '181', '60.66', '1']
c = []

# try-except 구문을 사용해서 정수 실수 구분
def t_float(n):
  try:
    int(n)
    return True
  except:
    return False

# 문자열인지 아닌지 구분

for idx,i in enumerate(a):
  if i.isdigit():
    print(f"{idx}번째 {i}는 숫자입니다.")
  else:
    print(f"{idx}번째 {i}는 문자입니다.")

# 숫자로 변경
for i in b:
  if t_float(i): 
    i = int(i)
  else: 
    i= float(i)
  c.append(i)
print(c)

# b의 리스트 float변경
# b의 형태가 모두 숫자 -> float
# for i in b:
#   c.append(float(i))
# print(c)