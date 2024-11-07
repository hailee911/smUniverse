a_list = ['서울의 봄',100,'2024-11-07']
# with open('d1107/s.txt','w',encoding='utf-8') as f:
#   a_title = ['제목','관객수','날짜']
#   f.write(','.join(a_title)+'\n')
#   for i in range(10):
#     f.write(','.join(a_list)+'\n')

with open('d1107/s3.csv','w',encoding='utf-8') as f:
  a_title = ['제목','관객수','날짜']
  f.write('제목,관객수,날짜\n')
  for i in range(10):
    f.write(f'{a_list[0]},{a_list[1]},{a_list[2]}\n')

  print('프로그램 완료')
  
