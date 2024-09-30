stu_title = ['번호', '이름', '국어', '영어', '수학', '과학', '합계', '평균']
stu_datas = [
    [1, '최승철', 100, 100, 100, 99],
    [2, '김민규', 100, 99, 98, 99],
    [3, '이도겸', 80, 100, 90, 99],
    [4, '권호시', 80, 100, 90, 99],
    [5, '문준휘', 80, 100, 90, 99]
]

# 합계와 평균 추가
for student in stu_datas:
    total = sum(student[2:6])
    average = total / 4
    student.append(total)
    student.append(round(average, 2))  # 소수점 둘째 자리까지 반올림

# 출력
print("------------------------------------------------------------")
print(f"{stu_title[0]:<5}{stu_title[1]:<10}{stu_title[2]:<6}{stu_title[3]:<6}{stu_title[4]:<6}{stu_title[5]:<6}{stu_title[6]:<6}{stu_title[7]:<6}")
print("------------------------------------------------------------")
for student in stu_datas:
    print(f"{student[0]:<5}{student[1]:<10}{student[2]:<6}{student[3]:<6}{student[4]:<6}{student[5]:<6}{student[6]:<6}{student[7]:<6}")
