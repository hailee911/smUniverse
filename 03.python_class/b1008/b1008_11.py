ss = "파이썬 수업중 type 문자열 type,정수형 type,실수형 type,논리형 type이 있습니다."

sss = ss.replace(" ","")
print(sss)

a_str = "파이썬"
a = "-".join(a_str)
print(a)

# idx = ss.find("type")+1
# print(ss.find("type",idx))

# i_str = input("글자를 입력하세용. >> ")
# if  i_str in ss:
#   print("있습니다.")
# else:
#   print("없습니다.")

# 위치값 - find 없을때 -1
# idx = ss.find(i_str)
# print("위치값 : ", idx)

# 검색 글자 개수 - count
# idx = ss.count(i_str)
# print("개수 : ", idx)

# type의 위치값을 모두 출력하시오. 머리 빠개질듯

# idx = 0
# search = input("검색할 단어를 입력하세용. >> ")
# a_list = []
# for i in range(ss.count(search)):
#   num = ss.find(search, idx) # 0번부터 시작 - 위치값 :  [8, 15, 22, 29, 36]
#   a_list.append(num)
#   idx = num+1

# print(f"검색개수: {len(a_list)}, 위치값 : {a_list}")
    

# 위치값 - index 없을때 에러
# idx = ss.index(i_str)
# print("위치값 : ", idx)


# 1-20 중에 3의 배수만 리스트에 추가하시오.
# a_list = []
# for i in range(1,21):
#   if i % 3 == 0:
#     a_list.append(i)

# print(a_list)

# 리스트 내포 (한줄 포문)
# [ 값 for문 조건문]
# b_list = [i for i in range(1,21) if i%3 == 0]
# print(b_list)

# aArr = [1,2,3,4,5]
# # a_list = [1,4,9,16,25]
# # 리스트 내포
# a_list = [i*i for i in aArr]

# print(a_list)