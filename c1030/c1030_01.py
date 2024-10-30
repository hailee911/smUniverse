import oracledb
import random
import smtplib
from email.mime.text import MIMEText

def connects():
  user = 'ora_user'
  pw = '1111'
  dsn = 'localhost:1521/xe'
  try:
    conn = oracledb.connect(user=user,password=pw,dsn=dsn)
  except Exception as e: print('예외발생 : ',e)
  return conn



while True:
  print('[ 커뮤니티 ]')
  print('1. 로그인')
  print('2. 비밀번호 찾기')
  print('3. 회원가입')
  print('0. 프로그램 종료')

  print('-'*30)

  choice = input('원하는 번호를 입력하세요.>> ')

  if choice == "1":
    print('[ 로그인 ]')
    user_id = input("아이디를 입력하세요.>> ")
    user_pw = input("패스워드를 입력하세요.>> ")

    # db 접속
    conn = connects()
    cursor = conn.cursor()
    sql = "select * from member where id =:id and pw =:pw"
    cursor.execute(sql, id=user_id, pw=user_pw)
    row = cursor.fetchone() # None
    print(row)
    if row != None:
      print(f'로그인 성공! {row[2]} 님 환영합니다.')
    else:
      print('아이디 또는 패스워드가 일치하지 않습니다. 정확히 입력하세요.')
    cursor.close()
    
    print('[ 학생성적 프로그램에 접속합니다. ]')
    # # # 프로그램 구현 # # #
  elif choice == "2":
    print('[ 비밀번호 찾기 ]')
    search = input('해당 아이디를 입력하세요.>> ')
    # 아이디 있는지 확인
    conn = connects()
    cursor = conn.cursor()
    sql = "select * from member where id=:id"
    cursor.execute(sql, id=search)
    row = cursor.fetchone()
    print(row)
    if row != None:
      print('아이디가 존재합니다. 임시패스워드를 발급합니다.')
      # 1. 임시비밀번호를 생성해서 
      # 2. 이메일로 보냅니다 
      # 3. 아이디에 비밀번호를 임시비밀번호를 수정합니다.
      # 4. 임시번호로 로그인을 했을 경우 로그인 성공이 어쩌구
      a = random.randrange(0,1000)
      ran_num = f"{a:04}"
      # print(ran_num)
      # 메일보내기
      smtpName = "smtp.naver.com"
      smtpPort = 587

      # 자신의 네이버메일주소,pw, 받는사람이메일주소
      sendEmail = "idy0911@naver.com"
      pw = "TVEYKS1G8REX"
      recvEmail = "idy0911@naver.com"

      title = "임시 비밀번호 생성"
      content = f"임시 비밀번호 : {ran_num}"

     # 설정
      msg = MIMEText(content)
      msg['Subject'] = title
      msg["From"] = sendEmail
      msg['To'] = recvEmail
      # 서버이름,서버포트
      s = smtplib.SMTP(smtpName,smtpPort)
      s.starttls()
      s.login(sendEmail,pw)
      s.sendmail(sendEmail,recvEmail,msg.as_string())
      s.quit()
      # 메일발송 완료
      print("메일로 임시 비밀번호를 발송했습니다. 확인 후 비밀번호를 업데이트 해주세요.")

      sql = "update member set pw =:pw where id =:id"
      cursor.execute(sql, id=search, pw=ran_num)
      conn.commit()

      print('비밀번호가 업데이트 되었습니다.')
      cursor.close()

    else:
      print('존재하지 않는 아이디입니다.')
      cursor.close()
  elif choice == "3":
    pass
  elif choice == "0":
    print("프로그램 종료합니다.")
    break
  