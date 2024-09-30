stu_title = ['번호', '이름', '국어', '영어', '수학', '과학', '합계', '평균']
stu_datas = [
    [1, '최승철', 100, 100, 100, 99],
    [2, '김민규', 100, 99, 98, 99],
    [3, '이도겸', 80, 100, 90, 99],
    [4, '권호시', 80, 100, 90, 99],
    [5, '문준휘', 80, 100, 90, 99]
]

for student in stu_datas:
    total = sum(student[2:6])  # 과목 점수의 합계
    average = total / 4        # 과목 수로 나누어 평균 계산
    student.append(total)      # 합계 추가
    student.append(average)    # 평균 추가

# 결과 확인
for student in stu_datas:
    print(student)





