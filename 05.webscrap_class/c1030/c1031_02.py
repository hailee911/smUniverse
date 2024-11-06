# import oracledb

# def connects():
#   user = 'ora_user'
#   pw = '1111'
#   dsn = 'localhost:1521/xe'
#   try:
#     conn = oracledb.connect(user=user,password=pw,dsn=dsn)
#   except Exception as e: print('예외발생 : ',e)
#   return conn

#  # db 접속
# conn = connects()
# cursor = conn.cursor()

# user_id = input("아이디를 입력하세요.>> ") #eee
# user_pw = input("패스워드를 입력하세요.>> ") #2222

# sql = "update member set pw =:pw where id =:id"
# cursor.execute(sql, id=user_id, pw=user_pw)
# conn.commit()

# print('파일이 수정되었습니다.')
# cursor.close()


# 임시비밀번호 생성
import random
a = random.randrange(0,1000)
ran_num = f"{a:04}"
print(ran_num)
