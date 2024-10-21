while True:
  no = input("번호를 입력하세요. >> ")
  if no == "0":
    break
  name = input("이름을 입력하세요. >> ")
  kor = int(input("국어점수를 입력하세요. >> "))
  eng = int(input("영어점수를 입력하세요. >> "))
  math = int(input("수학점수를 입력하세요. >> "))
  total = kor+eng+math
  avg = round(total/3,2)
  rank = 0
  data = f"{no},{name},{kor},{eng},{math},{total},{avg},{rank}\n"
  f = open('b1016/a.txt','a',encoding='utf-8')
  f.write(data)