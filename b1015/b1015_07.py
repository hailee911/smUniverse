students = [
  {"no":1,"name":"홍길동","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":0},
  {"no":2,"name":"유관순","kor":80,"eng":80,"math":85,"total":245,"avg":81.67,"rank":0},
  {"no":3,"name":"이순신","kor":90,"eng":90,"math":91,"total":271,"avg":90.33,"rank":0},
  {"no":4,"name":"강감찬","kor":60,"eng":65,"math":67,"total":192,"avg":64.00,"rank":0},
  {"no":5,"name":"김구","kor":100,"eng":100,"math":84,"total":284,"avg":94.67,"rank":0},
]

# key_1 = ['no','name','kor','eng','math','total','avg','rank']

stu_1 = "6,홍길자,100,100,100,300,100.0,0"
sArr = stu_1.split(",")

# 문자열 -> 리스트변경 -> 타입을 변경
for i,s in enumerate(sArr):
  if str.isdigit(s): # int타입이 변경이 가능한지??
    sArr[i] = int(s)
sArr[6] = float(sArr[6])   

students.append(sArr)

print(students)

