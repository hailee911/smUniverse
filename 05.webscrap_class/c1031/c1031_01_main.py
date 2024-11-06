import oracledb
import func # 파일 불러오기



while True:
  # 시작화면 출력
  choice = func.screen()

  if choice == "1":
    row = func.memLogin()

    if row == None:
      print("아이디가 존재하지 않습니다. 다시 입력하세요!")
      break
  if choice == "2":
    func.search_pw()
