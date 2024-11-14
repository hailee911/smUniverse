# Student 클래스 생성 후
# 데이터를 직접 입력을 받아, 클래스 선언 후 저장
# 번호 - 자동부여, 이름, 국어, 영어, 수학, 합계, 평균, 등수(= 0 고정)
# 클래스 전체 출력
# 클래스 수정

# [ 학생 성적 프로그램 ]
# 1. 학생 성적 입력
# 2. 학생 성적 출력
# 3. 학생 성적 수정
# Student.students 리스트
# for s in Students.students:
#   print(s)

# class Student():
#   def __init__(self):
#     pass

# while True:
#   print("[ 학생 성적 프로그램 ]")
#   print("1. 학생 성적 입력")
#   print("2. 학생 성적 출력")
#   print("3. 학생 성적 수정")
#   choice = int(input("번호를 입력하세요. >> "))
#   if choice == 1:
#     pass
#   elif choice == 2:
#     pass
#   elif choice == 3:
#     pass
#   elif choice == 4:
#     print("프로그램 종료")
#     break


# chat gpt ver.
class Student:
    students = []  # 모든 학생 정보를 저장할 리스트
    id_counter = 1  # 학생 번호 자동 부여를 위한 카운터

    def __init__(self, name, korean, english, math):
        self.id = Student.id_counter
        self.name = name
        self.korean = korean
        self.english = english
        self.math = math
        self.total = korean + english + math
        self.average = self.total / 3
        self.rank = 0  # 초기 등수는 0
        Student.id_counter += 1  # 다음 학생 번호를 위해 증가

    def __str__(self):
        return f"ID: {self.id}, 이름: {self.name}, 국어: {self.korean}, 영어: {self.english}, 수학: {self.math}, 합계: {self.total}, 평균: {self.average:.2f}, 등수: {self.rank}"

while True:
    print("[ 학생 성적 프로그램 ]")
    print("1. 학생 성적 입력")
    print("2. 학생 성적 출력")
    print("3. 학생 성적 수정")
    print("4. 프로그램 종료")
    
    choice = int(input("번호를 입력하세요. >> "))
    
    if choice == 1:
        name = input("이름을 입력하세요: ")
        korean = int(input("국어 점수를 입력하세요: "))
        english = int(input("영어 점수를 입력하세요: "))
        math = int(input("수학 점수를 입력하세요: "))
        student = Student(name, korean, english, math)
        Student.students.append(student)
        print(f"{student.name} 학생의 성적이 입력되었습니다.")

    elif choice == 2:
        if Student.students:
            print("\n[ 학생 성적 목록 ]")
            for s in Student.students:
                print(s)
        else:
            print("등록된 학생이 없습니다.")

    elif choice == 3:
        student_id = int(input("수정할 학생의 ID를 입력하세요: "))
        student_found = next((s for s in Student.students if s.id == student_id), None)
        
        if student_found:
            print(f"수정할 학생: {student_found.name}")
            student_found.korean = int(input("새로운 국어 점수를 입력하세요: "))
            student_found.english = int(input("새로운 영어 점수를 입력하세요: "))
            student_found.math = int(input("새로운 수학 점수를 입력하세요: "))
            student_found.total = student_found.korean + student_found.english + student_found.math
            student_found.average = student_found.total / 3
            print(f"{student_found.name} 학생의 성적이 수정되었습니다.")
        else:
            print("해당 ID의 학생을 찾을 수 없습니다.")

    elif choice == 4:
        print("프로그램 종료")
        break
    
    else:
        print("잘못된 입력입니다. 다시 시도하세요.")
