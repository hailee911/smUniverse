students = []
no = 0
rank = 0
title = ("번호\t이름\t국어\t영어\t수학\t합계\t평균\t순위")


while True:
  print("[ 학생성적프로그램 ]")
  print("-"*60)
  print("1. 학생성적입력")
  print("2. 학생성적출력")
  print("3. 학생성적수정")
  print("4. 학생성적검색")
  print("5. 학생성적삭제")
  print("6. 등수처리")
  print("0. 프로그램 종료")
  print("-"*60)
  choice = input("원하는 번호를 입력하세요.(0.종료)>> ")

  if choice == "1":
    print("***")
    print("[ 학생 성적 입력 ] ")
   
    while True:
      print()
      name = input("학생 이름을 입력하세요. (0. 메뉴로 돌아가기) >> ")
      if name == "0":
        print("성적 입력을 취소했습니다. 메뉴로 돌아갑니다.")
        print("***")
        break
      kor = int(input("국어 점수를 입력하세요. >>"))
      eng = int(input("영어 점수를 입력하세요. >>"))
      math = int(input("수학 점수를 입력하세요. >>"))
      total = kor+eng+math
      avg = round(total/3, 2)
      no += 1
      students.append([no, name, kor, eng, math, total, avg, rank])

  elif choice == "2":
    print("***")
    print("[ 학생 성적 출력 ] ")
    print()
    print(title)
    print("-"*60)
    for stu in students:
      for s in stu:
        print(s, end="\t") 
      print()
    print()
    print("***") 

  elif choice == "3":
    print("***")
    print("[ 학생 성적 수정 ] ")
    print()
    name = input("성적을 수정할 학생 이름을 입력하세요. (0. 메뉴로 돌아가기) >> ")
    if name == "0":
      print("성적 수정을 취소했습니다. 메뉴로 돌아갑니다.")
      print("***")
      break
    for stu in students:
      if name == stu[1]:
        print(f"{name} 학생을 찾았습니다.")
        print("***")
        print("1. 국어")
        print("2. 영어")
        print("3. 수학")
        print("0. 수정 취소")
        print("-"*60)
      # elif name != stu[1]:
      #   print(f"{name} 학생이 없습니다.")

        choice = input("수정할 과목을 선택하세요. >> ")
        if choice == "1":
          print(f"기존 국어 성적 : {stu[2]}")
          kor = int(input("국어 성적 입력 >> "))
          stu[2] = kor
          stu[5] = stu[2]+stu[3]+stu[4]
          stu[6] = round(stu[5]/3, 2)
          print("수정이 성공적으로 되었습니다.")
          print("***")
        elif choice == "2":
          print(f"기존 영어 성적 : {stu[3]}")
          eng = int(input("영어 성적 입력 >> "))
          stu[3] = eng
          stu[5] = stu[2]+stu[3]+stu[4]
          stu[6] = round(stu[5]/3, 2)
          print("수정이 성공적으로 되었습니다.")
          print("***")
        elif choice == "3":
          print(f"기존 수학 성적 : {stu[4]}")
          math = int(input("수학 성적 입력 >> "))
          stu[4] = math
          stu[5] = stu[2]+stu[3]+stu[4]
          stu[6] = round(stu[5]/3, 2)
          print("수정이 성공적으로 되었습니다.")
          print("***")
        elif choice == "0":
          print("성적 수정이 취소되었습니다. 메뉴로 돌아갑니다.")
          print("***")
          break

  elif choice == "0":
    print("***")
    print("프로그램을 종료합니다.")
    print("***")
    break  


  