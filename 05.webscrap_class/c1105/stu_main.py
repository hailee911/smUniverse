import stu_func as f

while True:
  choice = f.mainpage()

  if choice == '1':
    f.stu_insert()

  elif choice == '2':
    f.stu_output()

  elif choice == '3':
    f.stu_search()

  elif choice == "4":
    f.stu_order()
    
  elif choice == "5":
    f.stu_rank()

  elif choice == "0":
    print("프로그램을 종료합니다.")
