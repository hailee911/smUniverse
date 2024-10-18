# class - variable & function

# 학생 1명의 정보 - class로 변경
# 학생전체리스트 - class로 변경
students = [
  {"no":1,"name":"홍길동","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":0},
  {"no":2,"name":"유관순","kor":80,"eng":80,"math":85,"total":245,"avg":81.67,"rank":0},
  {"no":3,"name":"이순신","kor":90,"eng":90,"math":91,"total":271,"avg":90.33,"rank":0},
  {"no":4,"name":"강감찬","kor":60,"eng":65,"math":67,"total":192,"avg":64.00,"rank":0},
  {"no":5,"name":"김구","kor":100,"eng":100,"math":84,"total":284,"avg":94.67,"rank":0},
]

s_title = ['번호','이름','국어','영어','수학','합계','평균','등수']
s_t = ['no', 'name', 'kor', 'eng', 'math', 'total', 'avg', 'rank']

print("[ 학생 성적 출력 ]")
for st in s_title:
  print(st, end="\t")
print()
print("-"*80)
for i, s in enumerate(students):
  for i in range(len(s_t)):
    print(f"{s[s_t[i]]}",end='\t')
  print()

# 입력함수
def stu_chg(no,name,kor,eng,math):
  return {'no':no,'name':name,'kor':kor,'eng':eng,'math':math,'total':(kor+eng+math),'avg':round((kor+eng+math)/3, 2)}

print("[ 학생 성적 입력 ]")
no = 6
name = "김유신"
kor = 100
eng = 100
math = 100
# student리스트에 추가 (stu_chg() -> dict 타입)
students.append(stu_chg(no,name,kor,eng,math))
