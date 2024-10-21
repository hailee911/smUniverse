subject = ['이름','국어','영어','수학','합계','평균']
students = []

while True:
  print("1. 학생성적입력")
  print("2. 학생성적출력")
  print("3. 학생성적수정")
  choice = input("원하는 번호를 입력하세요.>> ")
  if choice == "1":
    name = input("이름을 입력하세요.>> ")
    score = [] # 국어 영어 수학
    score.append(name)
    sum = 0
    for i in range(len(subject[1:-2])):
      num = int(input(f"{subject[i+1]}점수를 입력하세요.>> "))
      score.append(num)
      sum += num
    avg = round(sum/len(subject[1:-2]),2)
    
    score.append(sum)
    score.append(avg)
    students.append(dict(zip(subject,score)))
    print(students)

  elif choice == "2":
    print("[ 학생 성적 출력 ]")
    for s in students:
      print(s, end="\n")
  elif choice == "3":
    
    search = input("찾고자하는 이름을 입력하세요.>> ")
    for s in students:
      if s['이름'] == search:
        print('[ 수정 과목 선택 ]')
        for i in range(len(subject[1:-2])):
          print(f"{i+1}. {subject[i+1]}")
        print("0.이전화면이동")
        choice = int(input("원하는 번호를 입력하세요.>> "))
        for c in range(len(subject[1:-2])):
          if choice == c+1:
            sum = 0
            print(f"현재 {subject[c+1]} 점수 :",s[subject[c+1]])
            s[subject[c+1]] = int(input("새로운 성적을 입력하세요.>> "))
            s[subject[-2]] = 0
            for n in range(len(subject[1:-2])):
              s[subject[-2]] += s[subject[n+1]]
            s[subject[-1]] = round(s[subject[-2]]/3, 2)

