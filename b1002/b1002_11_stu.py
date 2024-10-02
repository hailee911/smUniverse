students = [
  [1, '이다영', 100,90,99],
  [2, '최민기', 100,100,99],
  [3, '이석민', 100,100,99],
  [4, '권순영', 100,90,99],
  [4, '전원우', 100,90,99]
]

# 합계, 평균 추가
for s in students:
  s.append(s[2]+s[3]+s[4])
  s.append(round((s[2]+s[3]+s[4])/3 ,2))
  

cnt = 0
search = input("찾고자하는 학생이름을 입력하세요.")
for s in students:
  # 찾는 학생이 있으면 찾는 학생 이름이 있습니다.
  # cnt = 1
  if s[1] == search:
    print("찾는 학생이 있습니다.")
    print(s)
    cnt = 1
    break

if cnt == 0:
  print("찾고자 하는 학생 이름이 없습니다.")