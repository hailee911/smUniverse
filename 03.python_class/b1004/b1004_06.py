a_list = ['홍길동','유관순','이순신']

for idx , i in enumerate(a_list):
  a_list(idx) = (i,"님")

print(a_list)



# a_list = [1,2,3,4,5]
# # a_list = [1*1,2*2,3*3,4*4,5*5]
# print(a_list)
# # 리스트의 값을 변경해서 리스트에 저장
# # for idx, a in enumerate(a_list):
# #   a_list[idx] = a*a
# # print(a_list)


# # (축약) 리스트의 값을 변경해서 리스트에 저장 - 리스트 내포, 한줄 for문
# a_list = [i*i for i in a_list]
# print(a_list)

# print(a_list)
# a_list[1] = 100
# print(a_list)


# 없는 list 위치 값 수정 시 에러
# a_list[5] = 1000
# print(a_list)

# # 리스트 슬라이싱 0부터 4앞까지(3번까지)
# print(a_list[0:4])

# # 리스트 범위보다 넘어서 출력하려면, 에러가 나지 않고 출력은 됨.
# # 단 범위까지만 출력 됨.
# print(a_list[0:10])



# enumerate() 함수
# a_list = ['홍길동','유관순','이순신','강감찬','김구','김유신','홍길자']

# # for문으로 출력
# for a in a_list:
#   print(a)

# # enumerate()함수 - index번호를 출력 index,value
# for i,a in enumerate(a_list):
#   print(i+1,":",a)

# print(a_list)