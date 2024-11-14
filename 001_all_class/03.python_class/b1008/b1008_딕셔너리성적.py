students = []

# 학생성적 입력부분을 구현하시오.
# dict 타입으로 입력을 할 것
# 번호,이름,국어,영어,수학,합계,평균,등수
# 입력이 완료되면 출력이 바로 되도록 하시오.

no = 1
while True:
  # 학생 정보를 입력받기
  
  name = input("이름 (0. 종료): ")
  if name == "0":
      break
  kor = int(input("국어 점수: "))
  eng = int(input("영어 점수: "))
  math = int(input("수학 점수: "))

  # 합계, 평균, 등수 계산
  total = kor + eng + math
  avg = total / 3
  rank = 0  # 초기 등수는 0으로 설정

  # 학생 정보를 딕셔너리로 만들어 리스트에 추가
  student = {
      "no": no,
      "name": name,
      "kor": kor,
      "eng": eng,
      "math": math,
      "total": total,
      "avg": round(avg, 2),  # 소수점 둘째자리까지
      "rank": rank
  }
  students.append(student)
  no += 1

  # 입력한 학생 정보 출력
  print(student)

# 모든 학생의 성적 출력
print("\n모든 학생의 성적:")
for student in students:
    print(student)
