# 오라클 db에서는 타입 결정
# 문자형(숫자만) 타입 + 숫자와 사칙연산 됨
# 파이썬에서 호출한 타입의 결과값이 어떻게 되는지 확인

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

# db 접속
conn = connects()
cursor = conn.cursor()
# num,num,varchar,varchar
sql = "select no,kor,to_char(kor,'00000000'),to_char(kor_mark ,'999,999,999') from chart2"
cursor.execute(sql)
rows = cursor.fetchall()

for row in rows:
  # print(f'두수의 합 : {row[1]+row[2]}') # chart; 오라클에서는 계산됨 파이썬 안됨
  print(row)

print('검색완료')
conn.close()