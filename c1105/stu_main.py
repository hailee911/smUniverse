import stu_func as f

while True:
  choice = f.mainpage()

  if choice == '1':
    f.stu_insert()

  elif choice == '2':
    f.stu_print()

  elif choice == '3':
    f.stu_search()


  elif choice == '0':
    print("프로그램 종료")
    break
