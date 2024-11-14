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

s_title = ['번호','이름','국어','영어','수학','합계','평균','등수','등록일']

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
  print('4. 학생 성적 정렬')
  print('5. 등수처리')
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
    print('[ 학생 성적 출력 ]')
    conn = connects()
    cursor = conn.cursor()
    sql = "select name,kor,eng,math,total,round(avg,2),rank,to_char(sdate,'yyyy/mm/dd') from students"
    cursor.execute(sql)
    rows = cursor.fetchall()
    if len(rows) < 1:
      print('데이터가 없습니다.')
      break
    for row in rows:
      print(row)

  elif choice == '3':
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
      for row in rows:
        for i in row:
          print(i,end='\t')
        print()
      print()

  elif choice == "4":
    print("[ 학생성적 정렬 ]")
    print("1.이름순차정렬")      
    print("2.이름역순정렬")
    print("2.이름역순정렬")
    choice  = input("원하는 번호를 입력하세요.>> ") 
    if choice == "1":
      sql = "select no,name,kor,eng,math,total,round(avg,2),\
            rank,to_char(sdate,'yyyy-mm-dd') \
            from students order by name"
    elif choice == "2":
      sql = "select no,name,kor,eng,math,total,round(avg,2),\
            rank,to_char(sdate,'yyyy-mm-dd') \
            from students order by name desc"
    elif choice == "3": #합계순차정렬
      sql = "select no,name,kor,eng,math,total,round(avg,2),\
            rank,to_char(sdate,'yyyy-mm-dd') \
            from students order by total"
    elif choice == "4": #합계역순정렬
      sql = "select no,name,kor,eng,math,total,round(avg,2),\
            rank,to_char(sdate,'yyyy-mm-dd') \
            from students order by total desc"
          
    ##### 출력부분 #####
    # db연결
    conn = connects()
    cursor = conn.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    print(f"[ 개수 : {len(rows)} ]")
    for s in s_title:
      print(s,end='\t')
    print()  
    print("-"*80)
    if len(rows)<1: 
      print("데이터가 없습니다.")
      break
    for row in rows:
      for r in row:
        print(r,end="\t")
      print()
    print()
    print("데이터 출력완료!") 
    
  elif choice =="5":
    print("[ 학생등수처리 ]")
    sql = "update students a set rank = (\
          select ranks from \
      ( select no,rank() over(order by avg desc) ranks from students\
      ) b where a.no = b.no )"
      
    ##### 출력부분 #####
    
    # db연결
    conn = connects()
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    print("등수처리가 완료되었습니다.")
    print()
    #----------------------------------
    sql = "select no,name,kor,eng,math,total,round(avg,2),rank,to_char(sdate,'yyyy-mm-dd') from students"
    cursor.execute(sql)
    rows = cursor.fetchall()
    print(f"[ 개수 : {len(rows)} ]")
    for s in s_title:
      print(s,end='\t')
    print()  
    print("-"*80)
    if len(rows)<1: 
      print("데이터가 없습니다.")
      break
    for row in rows:
      for r in row:
        print(r,end="\t")
      print()
    print()
    print("데이터 출력완료!")  
  elif choice == "0":
    print("프로그램을 종료합니다.")
    break

# conn = connects()
# cursor = conn.cursor()
# sql = ''
# cursor.execute(sql)
# row = cursor.fetchone()
