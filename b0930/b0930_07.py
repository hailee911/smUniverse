stu_title = ['번호','이름','국어','영어','수학','과학','합계','평균']
stu_datas = [
  [1,'최승철', 100,100,100,99],
  [2,'김민규', 100,99,98,99],
  [3,'이도겸', 80,100,90,99],
  [4,'권호시', 80,100,90,99],
  [5,'문준휘', 80,100,90,99]
]

print("                   - 학생성적 프로그램 -")
print("-"*60)

for s_t in stu_title:
  print(s_t, end="\t")
print()
print("-"*60)

for s in stu_datas:
  print(s[0], end="      ")
  print(s[1], end="\t ")
  print(s[2], end="\t")
  print(s[3], end="\t")
  print(s[4], end="\t ")
  print(s[5], end="\t")
  print(s[2]+s[3]+s[4]+s[5], end="\t")
  print((s[2]+s[3]+s[4]+s[5])/4, end="\n")