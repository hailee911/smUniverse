# employees 테이블에서 이름이 a가 포함되어 있는 이름 모든 컬럼 출력
import oracledb

# db 연결 함수선언 #
def connections():
  try:
    conn = oracledb.connect(user="ora_user",password='1111',dsn='localhost:1521/xe')
    print("db연결: ",conn.version)
  except Exception as e: print('예외발생 : ',e)
  return conn

# 함수호출 #
conn = connections()
cursor = conn.cursor()

# 월급 4000 ~ 8000 사이의 사원을 모두 출력하시오.
# sql = 'select * from employees where salary between 4000 and 8000'
# cursor.execute(sql)

sal1 = input("숫자 입력 >> ")
sal2 = input("숫자 입력 >> ")
sql = 'select employee_id,emp_name,salary from employees where salary between :sal1 and :sal2'
rows = cursor.execute(sql, sal1=sal1, sal2=sal2)


# search = input('검색할 이름을 입력하세요. >> ')

# search = '%'+search+'%'
# sql = "select * from employees where emp_name like :search"
# cursor.execute(sql,search=search)

title = ['employee_id','emp_name','salary']
a_list = []

# sql = 'select employee_id,emp_name,salary from employees'
# rows = cursor.execute(sql)
for row in rows:
  a_list.append(dict(zip(title,row)))

print(a_list)

cursor.close()

