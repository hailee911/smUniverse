import copy

name = ["홍길동","유관순","이순신"]
score = [100,90,80]

n_dic = dict(zip(name,score))
print(n_dic)

a = n_dic # 얕은 복사
a['홍길동'] = 0
# 깊은 복사 copy.deepcopy()
a = copy.deepcopy(n_dic)
print(n_dic)


# # 얕은 복사, 깊은 복사

# name = ["홍길동","유관순","이순신"]
# score = [100,90,80]

# # n = name # name의 값을 n에 복사 얕은 복사

# # n[2] = "김구" # n의 이순신 -> 김구로 변경

# # print(name) # ['홍길동', '유관순', '김구'

# name = ["홍길동","유관순","이순신"]
# n = name[:] # 깊은 복사
# n[2] = "김구"
# print(n)
# print(name)
