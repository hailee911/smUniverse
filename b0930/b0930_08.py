### list 추가방법 : append - 제일 뒤에 추가, insert - 원하는 위치에 추가

a_list = [1,2,3]
print(a_list)

a_list.append(4) 
print(a_list)
a_list.append(10)
print(a_list)

a_list.insert(0,50) # 0번째 위치에 50 추가
print(a_list)
a_list.insert(3, 20)
print(a_list)

### 삭제 : del - index 위치에 데이터 삭제 , remove - 데이터 값으로 삭제
del a_list[0]
print(a_list)
a_list.remove(20)
print(a_list)

stu = [1,'최승철', 100,100,100,99]
# 합계 평균 추가
stu.append(stu[2]+stu[3]+stu[4]+stu[5])
stu.append((stu[2]+stu[3]+stu[4]+stu[5])/5)
print(stu)