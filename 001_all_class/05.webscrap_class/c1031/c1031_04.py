### 입력한 달 이상의 입사한 사원을 출력하시오. ###
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

d_day = int(input('숫자를 입력하세요.>> '))
print(d_day)

# db 접속
conn = connects()
cursor = conn.cursor()
# num,num,varchar,varchar
sql = "select emp_name, to_char(hire_date,'yyyy-mm-dd') from employees where substr(hire_date,4,2) >= :month"
cursor.execute(sql, month = d_day)
rows = cursor.fetchall()

for row in rows:
  print(row)

print('검색완료')
conn.close()