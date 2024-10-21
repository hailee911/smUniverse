fruit = "사과,배,딸기,포도,복숭아,배,사과,배,딸기"

fruits = fruit.split(",") # list
# print(fruits)
# print(len(fruits))  # 9개

search = input("과일입력 : ")
# 리스트 인 경우 해당되는 인덱스를 출력하시오.
for idx, f in enumerate(fruits):
  if f == search:
    print(f"{search}의 위치 : {idx}")


# print(fruit.find('배', 0))
# print(fruit.find('배', 3+1))
# print(fruit.find('배', fruit.find('배',0)+1))
# print(fruit.find('배', 15+1))
# print(fruit.find('배', fruit.find('배', fruit.find('배',0)+1)+1))

# print(fruit.find("딸기", 0)) # 5
# print(fruit.find("딸기", 0)+1)
# print(fruit.find("딸기", 6))