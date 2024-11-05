import oracledb

# db 연결함수
def connects():
  user = 'ora_user'
  pw = '1111'
  dsn = 'localhost:1521/xe'
  try:
    conn = oracledb.connect(user=user,password=pw,dsn=dsn)
  except Exception as e: print('예외발생 : ',e)
  return conn

def mainpage():
  print('[ 학생 성적 프로그램 ]')
  print('1. 학생 성적 입력')
  print('2. 학생 성적 출력')
  print('3. 학생 성적 검색')
  print('4. 학생 성적 정렬')
  print('5. 등수처리')
  choice = input('원하는 숫자 입력>> ')
  return choice

def stu_insert():
    print('[ 학생 성적 입력 ]')
    name = input('이름을 입력하세요.>> ')
    kor = int(input('국어성적 입력>> '))
    eng = int(input('영어성적 입력>> '))
    math = int(input('수학성적 입력>> '))
    total = kor+eng+math
    avg = round(total/3,2)
    rank = 0
    conn = connects()
    cursor = conn.cursor()
    sql = 'insert into students values(students_seq.nextval,:name,:kor,:eng,:math,:total,:avg,:rank,sysdate)'
    cursor.execute(sql,name=name,kor=kor,eng=eng,math=math,total=total,avg=avg,rank=rank)
    conn.commit()
    conn.close()
    print(f'{name} 학생의 성적이 등록되었습니다.')

def stu_print():
  print('[ 학생 성적 출력 ]')
  conn = connects()
  cursor = conn.cursor()
  sql = "select name,kor,eng,math,total,round(avg,2),rank,to_char(sdate,'yyyy/mm/dd') from students"
  cursor.execute(sql)
  rows = cursor.fetchall()
  if len(rows) < 1:
    print('데이터가 없습니다.')
  for row in rows:
    print(row)

def stu_search():
  print('[ 학생 성적 검색 ]')
  name = input('찾고자 하는 학생의 이름을 입력하세요.>> ')
  conn = connects()
  cursor = conn.cursor()
  search = '%'+name+'%'
  sql = "select name,kor,eng,math,total,avg,rank,to_char(sdate,'yyyy/mm/dd') from students where name like :search"
  cursor.execute(sql, search=search)
  rows = cursor.fetchall()
  if rows is None:
    print('찾는 학생이 없습니다.')
  else:
    print(f'이름\t국어\t영어\t수학\t합계\t평균\t등수\t등록일')
    print('-'*70)
    for row in rows:
      for i in row:
        print(i,end='\t')
      print()
    print()