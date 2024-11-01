# 학생성적프로그램
# 1. 학생성적입력
# 2. 학생성적출력
# 3. 학생성적검색
# students 테이블 사용해서
# 시퀀스 students_seq 생성
# 번호 김유신, 99 98 96 합계 평균 등수 입력일
# 프로그램 작성.

import oracledb
import datetime

# db 연결함수
def connects():
  user = 'ora_user'
  pw = '1111'
  dsn = 'localhost:1521/xe'
  try:
    conn = oracledb.connect(user=user,password=pw,dsn=dsn)
  except Exception as e: print('예외발생 : ',e)
  return conn

while True:
  print('[ 학생 성적 프로그램 ]')
  print('1. 학생 성적 입력')
  print('2. 학생 성적 출력')
  print('3. 학생 성적 검색')
  choice = input('원하는 숫자 입력>> ')
  if choice == '1':
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
  elif choice == '2':
    print()

  elif choice == '3':
    name = input('찾고자 하는 학생의 이름을 입력하세요.>> ')
    conn = connects()
    cursor = conn.cursor()
    sql = "select name,kor,eng,math,total,avg,rank,to_char(sdate,'yyyy/mm/dd') from students where name = :name"
    cursor.execute(sql, name=name)
    row = cursor.fetchone()
    if row is None:
      print('찾는 학생이 없습니다.')
    else:
      print(row)

  elif choice == '0':
    print('프로그램 종료')
    break

# conn = connects()
# cursor = conn.cursor()
# sql = ''
# cursor.execute(sql)
# row = cursor.fetchone()
