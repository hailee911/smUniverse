students = [] # 학생 리스트

s_title = ["번호","이름","국어","영어","수학","합계","평균","등수"]
choice = 0 # 선택
stuNo = 0 # 학생 번호 생성
check = 0 # 체크 변수
count = 0 # 성적 처리 카운트 변수
stuNo = len(students) # 리스트에 학생이 있으면, 그 인원으로 변경 ( 삭제 이후 번호 이슈 )

# 프로그램 시작
while True:
  print("[ 학생 성적 프로그램 ]")
  print("-"*60)
  print("1. 학생 성적 입력")
  print("2. 학생 성적 출력")
  print("3. 학생 성적 수정")
  print("4. 학생 성적 검색")
  print("5. 학생 성적 삭제")
  print("6. 등수 처리")
  print("7. 학생 성적 정렬")
  print("0. 프로그램 종료")
  print("-"*60)
  choice = int(input("원하는 번호를 입력하세요. >> "))
  print("☆")
  if choice == 1:
    while True:
      print("[ 학생 성적 입력 ]")
      # 학생 성적 직접 입력
      print()
      no = stuNo + 1 # 리스트 -> 학생 수 1부터
      name = input(f"{no}번째 학생 이름을 입력하세요. (0. 이전 화면으로) >> ")
      if name == "0":
        print("성적 입력을 취소합니다.")
        print()
        break # 빠져나오기 -> 상단 메뉴로
      kor = int(input("국어 점수를 입력하세요. >>"))
      eng = int(input("영어 점수를 입력하세요. >>"))
      math = int(input("수학 점수를 입력하세요. >>"))
      print("★")
      total = kor + eng + math
      avg = round(total / 3, 2)
      rank = 0

      students.append( {"no":no, "name":name, "kor":kor, "eng":eng, "math":math, "total": total, "avg":avg, "rank": rank} )
      
      stuNo += 1 # 학생 수 1 증가
      print(f"{name}학생의 성적이 저장되었습니다.")

      print("★")

  elif choice == 2:
    print("[ 학생 성적 출력 ]")
    # 상단 타이틀 출력
    for title in s_title: 
      print(f"{title}\t", end="")
    print()
    print("="*60)
    # 학생 출력
    for s in students:
      for key in s:
        print(s[key], end="\t")
      print()
    print("★")

  elif choice == 3:
    print("[ 학생 성적 수정 ]")
    name = input("찾고자 하는 학생의 이름을 입력하세요. >> ")
    check = 0
    print()
    for s in students:
      if s["name"] == name: 
        check = 1
        # 학생 성적 수정 
        print(f"{name} 학생을 찾았습니다.")
        print("☆")
        print("[ 수정하고자 하는 과목 선택 ]")
        print("1. 국어 점수")
        print("2. 영어 점수")
        print("3. 수학 점수")
        print("0. 수정 취소")
        choice = int(input("원하는 번호를 입력하세요. >> "))
        print()
        if choice == 1:
          print("이전 국어 점수 : {}".format(s["kor"]))
          s["kor"] = int(input("변경 국어 점수 : "))
          
        elif choice == 2:
          print("이전 영어 점수 : {}".format(s["eng"]))
          s["eng"] = int(input("변경 영어 점수 : "))
        elif choice == 3:
          print("이전 수학 점수 : {}".format(s["math"]))
          s["math"] = int(input("변경 수학 점수 : "))
        elif choice == 0:
          print("수정을 취소합니다.")
          print("☆")
          break

        # 합계, 평균 다시 구해 업데이트
        s["total"] = s["kor"]+s["eng"]+s["math"]
        s["avg"] = round(s["total"]/3, 2)
        
        print(f"{name} 학생 성적이 수정되었습니다.")
        print("☆")

    if check == 0:
      print(f"{name} 학생이 없습니다.")
      print()
      print("☆")

  elif choice == 4:
    print("[ 학생 성적 검색 ]")
    check = 0
    name = input("찾고자 하는 학생의 이름을 입력하세요. >> ")
    print()
    for s in students:
      if s["name"] == name: 
        check = 1
        print(f"{name} 학생을 찾았습니다.")
        print("☆")
        for title in s_title: 
          print(f"{title}\t", end="")
        print()
        print("="*60)
        # 학생 출력
        for key in s:
          print(s[key],end="\t")
      print()
    # 모든 학생 비교가 끝난 후, check 확인
      if check == 0:
        print(f"{name} 학생이 없습니다.")
        print()
        print("☆")
  
  elif choice == 5:
    print("[ 학생 성적 삭제 ]")
    name = input("찾고자 하는 학생의 이름을 입력하세요. >> ")
    check = 0
    print()

    for idx, s in enumerate(students):
      if s["name"] == name:
        check = 1
        choice = int(input(f"{name} 학생 성적을 삭제하시겠습니까? (삭제시 복구불가)\n 1.삭제 2.취소 >> "))
        print("☆")
        if choice == 1:
          del students[idx]
          print(f"{name} 학생의 성적이 성공적으로 삭제되었습니다.")
          print()
        else:
          print(f"{name} 학생 성적 삭제가 취소되었습니다.")
          print()
          break

    # 모든 학생 비교가 끝난 후, check 확인
    if check == 0:
      print(f"{name} 학생이 없습니다.")
      print()
      print("☆")
        
  elif choice == 6:
    print("[ 등수 처리 ]")
    # 서로서로 비교해서 작으면 카운트 + 1
    for s in students:
      count = 1
      for st in students:
        if s["total"] < st["total"]:
          count += 1
      s["rank"] = count # 등수 입력
    print("등수 처리가 완료되었습니다.") 
    print("★")

  elif choice == 7:
    while True:
      print("[ 학생 성적 정렬 ]")
      print()
      print("1. 이름 순차 정렬")
      print("2. 이름 역순 정렬")
      print("3. 합계 순차 정렬")
      print("4. 합계 역순 정렬")
      print("5. 번호 순차 정렬")
      print("0. 이전페이지 이동")
      print("-"*40)
      choice = input("원하는 번호를 입력하세요. >> ")

      if choice == "1":
        students.sort(key=lambda x:x['name'])
      elif choice == "2":
        students.sort(key=lambda x:x['name'], reverse=True)
      elif choice == "3":
        students.sort(key=lambda x:x['total'])
      elif choice == "4":
        students.sort(key=lambda x:x['total'], reverse=True)
      elif choice == "5":
        students.sort(key=lambda x:x['no'])
      elif choice == "0":
        print("이전 페이지로 이동합니다.")
        break
      print("정렬이 완료되었습니다.")
  
  elif choice == 0:
    print("프로그램을 종료합니다.")
    break

