# 리스트
# in - 데이터가 있는지 확인
# count - 데이터 개수
# find - 데이터가 있는 위치, 없으면 - 1 (검색어, 시작위치, 끝위치)
# index - 데이터가 있는 위치, 없으면 에러

fruit = "사과,배,딸기,포도,복숭아,배,사과,배,딸기"
# 배가 있는지 위치를 모두 출력하시오.

search = input("과일 이름을 입력하세요.")
print("모든 글자 : ", fruit)

idx = 0
if fruit.count(search)>0:
  print(f"{search} 글자가 있습니다.")
  for i in range(fruit.count(search)):
    print(f"{search} 글자가 있는 위치 : ",fruit.find(search, idx))
    idx = fruit.find(search, idx)+1
else:
  print(f"{search}(이)라는 글자는 없습니다.")





# search = input("과일 이름을 입력하세요.")

# if search in fruit:
#   print("과일검색개수 : {}".format(fruit.count(search)))
#   print(fruit.index(search))
#   print(fruit.find(search))
# else:
#   print(f"{search}라는 글자가 없어요")
