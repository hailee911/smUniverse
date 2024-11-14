# 리스트


a = [1,2,3,4,5]
b = [50,100]
print(a[0:3]) # [1,2,3]
print(a[2:4]) # [3,4]
print(a[:3])  # [1,2,3]
print(a + b)  # [1,2,3,4,5,50,100]
# a.remove(5)
print(a.count(3)) # 리스트 안에 3이 몇개가 있는지 확인
a.insert(0, 200) # 0번째 200 삽입
a.clear() # [] 전체삭제
print(a)

# del a[0] # [2,3,4,5] - 0번째 삭제
# print(a)
# a[1:3] = []
# print(a) # [2,5]


# del(a) # list 자체 날리기




# a_list = [1,2,3,4,5]
# # b_list = a_list[::-1]
# # b_list = a_list 얕은 복사
# # print(a_list)
# # print(b_list)
# # a_list[0] = 100 a_list 값을 변경하면 b_list 값 변경
# # print(b_list)
# # print(a_list)

# b_list = a_list[:] # 깊은 복사
# a_list[0] = 100 # a_list의 값을 변경해도 b_list 값 변경이 안됨.
# print(a_list) 
# print(b_list) 

# 역순 출력 방법
# for i in range(1, 6):
#   print(a_list[-i])
# for i in range(len(a_list)):
#   print(a_list[(-(i+1))])



# # 문자열, 숫자-정수형, 실수형, 논리형
# a_list = [1,2,3.0,"안녕",True,False]
# print(a_list[0])
# print(a_list[-1])

#  a_list = []
# a = 1
# # 1-100 들어가 있는 리스트를 출력하시오.
# for i in range(100):
#   a_list.append(a)
#   a += 1

# print(a_list)



# a_list = []
# total = 0

# for i in range(7):
#   j = int(input(f"{i+1}번째 숫자를 입력하세요 >> "))
#   a_list.append(j)
#   total += j

# print(a_list)

# # for idx, a in enumerate(a_list):
# #   a = int(input(f"{idx+1}번째 숫자를 입력하세요. "))
# #   total += a

# print("합계 : ",total)