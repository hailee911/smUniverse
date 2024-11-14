# # 튜플
# # t = (1,2,3,4)
# # print(t[0])
# # # 튜플은 t(0) = 10 & (append) 안됨
# # print(len(t))

# # for i in t:
# #   print(i)

# # # 더하기 연산자로 추가 가능
# # t = t+(3,5)
# # # 곱하기 연산자 가능
# # tt = (1,2,3)
# # t = tt*2
# # print(t)

# # t = [1,2,4,6]
# # t.sort()
# # print(t)
# # t[1:3]
# # print(t+[3,7])
# # print(t)

# # t.extend([3,7]) # t에 반영이 됨


# aArr = [[1,2],[[1,2],[3,4]],[5,6],[7,8]]
# # a_list = [1,2,3,4,5,6,7,8]

# b_list = []
# for i in aArr:
#   if type(i) == list:
#     for j in i:
#       if type(j) == list:
#         for k in j:
#           b_list.append(k)
#       else:
#         b_list.append(j)
# print(b_list)

# a = '우유'
# b = '커피'
# c = ''

# # 치환
# a,b = b,a
# print(a,b)

# c = a
# a = b
# b = c
# print(a,b)

# 문자열을 tuple 타입 변경

# a_str = "abcdefu"
# # print(a_str)
# # print(a_str[1])

# a_tu = tuple(a_str)
# b_list = list(a_tu)
# print(a_tu)
# print(b_list)

a = ((1,2),(3,4),(5,6))
print(a[0][1])