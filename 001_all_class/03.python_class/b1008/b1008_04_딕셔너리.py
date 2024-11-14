# # 딕셔너리 생성

# # 리스트 타입
# # 튜플 타입 - 수정불가


# dic1 = {"번호":1,"이름":"홍길동","kor":100,"eng":100}

# # # 키를 입력하면 값을 출력
# # print(dic1["이름"])

# # 딕셔너리 추가 방법 - 없는 키를 입력하면 추가
# dic1["math"] = 90

# dic1['kor'] = 50

# # del(키) 삭제
# del(dic1['eng'])

# # print(dic1)


# # 없는 키 입력시 None -> 에러 안남
# # print(dic1.get("학번")) 

# # if dic1.get("이름") != None:
# #   print(dic1.get("이름"))

# # 모든 키값을 출력 dict_keys(['번호', '이름', 'kor', 'math'])
# # print(dic1.keys())

# for key in dic1.keys():
#   print(key, dic1[key])

# # 번호 1
# # 이름 홍길동
# # kor 50
# # math 90

# print(type(dic1.keys()))
# list(dic1.keys())

# print(type(list(dic1.keys())))
# # ['번호', '이름', 'kor', 'math']
# print(list(dic1.keys()))
# print(list(dic1.keys())[0])

# # 값만 출력 dict_values([1, '홍길동', 50, 90]) : class 객체 타입
# # 리스트 타입 변경 시 - [1, '홍길동', 50, 90]
# print(dic1.values())
# print(list(dic1.values()))

# # 키, 값 모두 출력 - dict_items([('번호', 1), ('이름', '홍길동'), ('kor', 50), ('math', 90)])
# print(dic1.items())


# # for 문으로 출력

# # 키 값만 출력
# for key in dic1:
#   print(key)

# # 키, 값 출력
# for key,val in dic1.items():
#   print(key, val)

# # 값만 출력
# for key in dic1:
#   print(dic1[key])

# # 평균이 없을때만 평균을 추가
# if '평균' not in dic1:
#   dic1['평균'] = 99.0

# print(dic1)

