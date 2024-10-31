import random
import oracledb
import smtplib
from email.mime.text import MIMEText

# db 연결함수
def connects():
  user = 'ora_user'
  pw = '1111'
  dsn = 'localhost:1521/xe'
  try:
    conn = oracledb.connect(user=user,password=pw,dsn=dsn)
  except Exception as e: print('예외발생 : ',e)
  return conn


def screen():
  print('[ 커뮤니티 ]')
  print('1. 로그인')
  print('2. 비밀번호 찾기')
  print('3. 회원가입')
  print('0. 프로그램 종료')

  print('-'*30)

  choice = input('원하는 번호를 입력하세요.>> ')
  return choice

def memLogin():
  print('[ 로그인 ]')
  user_id = input("아이디를 입력하세요.>> ")
  user_pw = input("패스워드를 입력하세요.>> ")
  # db 접속
  conn = connects()
  cursor = conn.cursor()
  sql = "select * from member where id=:id and pw=:pw"
  cursor.execute(sql, id=user_id, pw=user_pw)
  row = cursor.fetchone()

  if row == None:
    print("아이디가 존재하지 않습니다. 다시 입력하세요!")

  else:
    print('로그인 성공')
    return row

# 임시 비밀번호 함수 선언
def random_pw():
  a = random.randrange(0,10000)
  ran_num = f'{a:04}'
  print('랜덤 번호 :',ran_num)
  return ran_num

def search_pw():

  user_id = input("아이디를 입력하세요.>> ")
  conn = connects()
  cursor = conn.cursor()
  sql = "select * from member where id=:id"
  cursor.execute(sql, id=user_id)
  row = cursor.fetchone()

  input(f"{row[0]} 아이디가 존재합니다. 메일을 보내려면 enter를 입력하세요.")

  # 이메일 발송 함수 호출
  random_pw = emailSend(row[3])
  
  # 임시비밀번호를 update
  sql = "update member set pw =:pw where id=:id"
  cursor.execute(sql, pw=random_pw, id=user_id)

# 메일 발송 함수선언
def emailSend(email):
  smtpName = 'smtp.naver.com'
  smtpPort = 587

  sendEmail = 'idy0911@naver.com'
  pw = 'TVEYKS1G8REX'
  recvEmail = email

  title = '[ 메일발송 ] 임시비밀번호 안내'
  ran_num = random_pw()
  content = f'임시비밀번호 : {ran_num}'
  print(content)

  # 설정
  msg = MIMEText(content)
  msg['Subject'] = title
  msg['From'] = sendEmail
  msg['To'] = recvEmail

  # 서버이름 서버포트
  s = smtplib.SMTP(smtpName,smtpPort)
  s.starttls()
  s.login(sendEmail,pw)
  s.sendmail(sendEmail,recvEmail,msg.as_string())
  s.quit()

  # 메일발송완료
  print('메일이 발송되었습니다.')

  return ran_num