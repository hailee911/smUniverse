def operate(count):
  for i in range(count):
      print("한국어 인사 : 안녕하세요.")

while True:
  print("[ 외국어 인사 ]")
  print("1. 영어 인사")
  print("2. 일본어 인사")
  print("3. 중국어 인사")
  print("4. 프랑스 인사")
  choice = input("원하는 번호를 입력. >> ")
  count = int(input("한국어 반복회수를 입력. >> "))
  if choice == "1":
    operate(count)
    print("영어 인사 : 헬로우, (Hello)")
  elif choice == "2":
    operate(count)
    print("일본어 인사 : 오하이요, (Ohayo)")
  elif choice == "3":
    operate(count)
    print("중국어 인사 : 니하오,(Ni hao)")
  elif choice == "4":
    operate(count)
    print("프랑스 인사 : 봉주르,(Bonjour)")
