stu_key = ['no','name','kor','eng','math','total','avg','rank']
students = []
# 파일 읽기 - r
f = open('b1016/a.txt','r',encoding='utf-8')
while True:
  line = f.readline()
  if not line : break
  s = line.strip().split(",")
  for i in range(len(s)):
    if i == 1: continue
    elif i == 6: s[6] = float(s[6])
    else: s[i] = int(s[i])

  students.append(dict(zip(stu_key,s)))
  print(line.strip())

f.close()
print(students)
