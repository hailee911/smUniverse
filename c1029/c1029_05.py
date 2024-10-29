a = 1
b = 2

a_list = [a,b]
print(type(a_list))

b_list = [b]
print(type(b_list))

# a_tuple = (a,b)
# print(type(a_tuple))

# (a) 타입 int (a,) 타입 tuple 1개만 지정할때는 뒤에 , 넣어야함
# b_tuple = (a,)
# print(type(b_tuple))

name = '홍길동'

# 문자 변수 출력
print('안녕하세요. 이름은 %s'%name)

title = ['e_id','e_name','salary']
a = [
  (196, 'Alana Walsh', 3100.0),
  (125, 'Julia Nayer', 3200.0),
  (180, 'Winston Taylor', 3200.0),
  (194, 'Samuel McCain', 3200.0),
  (138, 'Stephen Stiles', 3200.0)
]

aa = []
for i in a:
  a = dict(zip(title,i))
  aa.append(a)

print(aa)