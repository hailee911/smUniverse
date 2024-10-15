import S_func





# --------------------------프로그램 시작-----------------------------------------
# 학생성적프로그램
while True:
  choice = S_func.title_program()        # 메뉴출력함수 호출
  if choice == "1":
    stuNo = S_func.stu_input(stuNo)      # 학생성적입력함수 호출
  elif choice == "2":
    S_func.stu_output()  # 학생성적출력함수 호출
  elif choice == "3":
    S_func.stu_update() # 학생성적수정함수 호출
  elif choice == "4":
    pass
  elif choice == "5":
    S_func.stu_delete()
  elif choice == "6":
    S_func.stu_rank()
  
  #-------------------------프로그램 끝-------------------------------------------
  # 4,7

  # elif choice == "4":
  #   print("[ 학생성적검색 ]")
  #   name = input("찾고자 하는 학생의 이름을 입력하세요.")
  #   chk = 0
  #   for s in students:
  #     if s[1] == name:
  #       # 학생출력
  #       # 상단타이틀 출력
  #       for title in S_func.s_title:
  #         print(f"{title}\t",end="")
  #       print()
  #       print("-"*60)
  #       print(f"{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}\t{s[4]}\t{s[5]}\t{s[6]:.2f}\t{s[7]}\n")
  #       print()
  #       chk = 1
  #   # 모든 학생 비교가 끝난 후, chk 확인
  #   if chk == 0:
  #     print(f"{name} 학생이 없습니다. 다시 입력하세요.")
    
  #------------------------------------------
  # elif choice == "7":
  #   while True:
  #     print("[ 학생성적 정렬 ]")
  #     print("1. 이름 순차정렬")
  #     print("2. 이름 역순정렬")
  #     print("3. 합계 순차정렬")
  #     print("4. 합계 역순정렬")
  #     print("5. 번호 순차정렬")
  #     print("0. 이전페이지 이동")
  #     print("-"*40)
  #     choice = input("원하는 번호를 입력하세요.>> ")
  #     if choice == "1":
  #       students.sort(key=lambda x:x['name'])
  #     elif choice == "2":
  #       students.sort(key=lambda x:x['name'],reverse=True)
  #     elif choice == "0":
  #       print("이전페이지로 이동합니다.")
  #       break
  #     print("정렬이 완료되었습니다.")
  elif choice == "0":
    print("[ 프로그램 종료 ]")
    print("프로그램을 종료합니다.")
    break