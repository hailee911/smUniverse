students = []
no = 1
s_title = ("번호\t이름\t국어\t영어\t수학\t총합\t평균\t등수")

# 학생성적프로그램
while True:
  print("[ 학생 성적 프로그램 ]")
  print("-" * 60)
  print("1. 학생성적입력")
  print("2. 학생성적출력")
  print("3. 학생성적수정")
  print("4. 학생성적검색")
  print("5. 학생성적삭제")
  print("6. 등수처리")
  print("0. 프로그램 종료")
  print("-" * 60)
  choice = input("원하는 번호를 입력하세요 . >> ")

  if choice == "1":

    print("[ 학생 성적 입력 ]")
    print()
    while True:
      name = input(f"{no}번째 학생 이름을 입력하세요. (메뉴로 돌아가기 : 0) >> ")
      if name == "0":
        print("메뉴로 돌아갑니다.")
        break
      kor = int(input("국어 점수 입력 >>"))
      eng = int(input("영어 점수 입력 >>"))
      math = int(input("수학 점수 입력 >>"))
      total = kor + eng + math
      avg = round(total/3, 2)
      rank = 0
      s = [no, name, kor, eng, math, total, avg, rank]
      students.append(s)
      print(students)
      no += 1

  elif choice == "2":

    print("[ 학생 성적 출력 ]")
    print()
    print(s_title)
    print("-"*60)
    for i in students:
      for s in i:
        print(s, end="\t")
      print()

  elif choice == "3":
    cnt = 0
    print("[ 학생 성적 수정 ]")

    print("[ 학생 성적 검색 ]")
    name = input("수정하고자 하는 학생 이름을 입력하세요. >> ")
    for i in students:
      if i[1] == name:
        print(f"{name} 학생을 찾았습니다.")
        print("[ 과목 선택 ]")
        print(" 1. 국어 점수 ")
        print(" 2. 영어 점수 ")
        print(" 3. 수학 점수 ")
        print(" 0. 수정 취소 ")
        choice = int(input("원하는 번호를 입력하세요. >> "))
        if choice == 1:
          print("현재 국어 점수 : ", i[2])
          i[2] = int(input("국어 점수를 입력하세요. >> "))
        elif choice == 2:
          print("현재 영어 점수 : ", i[3])
          i[3] = int(input("국어 점수를 입력하세요. >> "))
        elif choice == 3:
          print("현재 국어 점수 : ", i[4])
          i[4] = int(input("국어 점수를 입력하세요. >> "))
        elif choice == 0:
          print(f"{name} 학생의 성적 수정이 취소되었습니다.")
          cnt = 1
        if cnt == 0:
          i[5] = i[2]+i[3]+i[4]
          i[6] = round(i[5]/3, 2)
          print(f"{name} 학생의 성적이 변경되었습니다.")
        
          

  elif choice == "4":
    print("[ 학생 성적 검색 ]")
    name = input("찾고자 하는 학생 이름을 입력하세요. >> ")
    for i in students:
      if i[1] == name:
        print(f"{name} 학생을 찾았습니다.")
        print(s_title)
        print("-"*60)
        for s in i:
          print(s, end="\t")
      # 카운트 넣기
      else:
        print(f"{name} 학생을 찾지 못했습니다.")
        break
    print()
    print("-"*60)

  elif choice == "5":
    print("[ 학생 성적 삭제 ]")
    name = input("삭제하고자 하는 학생 이름을 입력하세요. >> ")
    for i in students:
      if i[1] == name:
        print(f"{name} 학생을 찾았습니다.")
        choice = input("이 학생의 성적을 삭제하시겠습니까? 예(1)/아니오(0) >> ")
        if choice == "1":
          print(f"{name} 학생의 성적을 삭제합니다.")
          students.remove(i)

        elif choice == "0":
          print("학생 성적 삭제를 취소했습니다.")
        


  elif choice == "0":
    print("프로그램을 종료합니다.")
    break


  # 미해결 부분
  # 학생을 찾지 못했습니다. -> 찾은 후 else 부분도 출력됨

  # 왜 되다가 안되는지 이해 x
  # 순위 (랭크) 초이스 부분 안만듬
  # 번호 리셋시키기