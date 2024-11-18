from django.shortcuts import render, redirect
from students.models import Student # 파일저장

# 학생 삭제
def delete(request, name):
  print("삭제정보 : ", name)
  Student.objects.get(name=name).delete()
  return redirect("students:list")

  

# 학생수정페이지 - url 매개변수로 데이터값을 전달받음
def modify(request,name):
  if request.method == "GET":
    print('modify 이름정보 : ',name)
    qs = Student.objects.filter(name=name)
    context = {'stu':qs[0]}
    return render(request, 'update.html',context)
  else:
    print('POST 호출')
    qs = Student.objects.get(name=name)
    name = request.POST['name']
    major = request.POST['major']
    grade = request.POST['grade']
    age = request.POST['age']
    gender = request.POST['gender']
    print("수정 modify 정보 : ", name,major,grade,age,gender)
    qs.major = major
    qs.grade = grade
    qs.age = age
    qs.gender = gender
    qs.save()
    return redirect('students:list')
  
    

# 학생수정페이지2 - 파라미터
def modify2(request):
  name = request.GET.get('name')
  print('modify2 이름정보 : ',name)
  return render(request, 'list.html')

# 학생수정페이지3 - appName 매개변수로 데이터값을 전달받음
def modify3(request,name):
  print('modify3 이름정보 : ',name)
  qs = Student.objects.filter(name=name)
  context = {'stu':qs[0]}
  return render(request, 'update.html',context)

# 학생상세페이지
def view(request, name):
  print("이름정보 : ",name) # 터미널 확인용
  qs = Student.objects.filter(name = name) # 1개 데이터-list, 없을경우 {}
  print(qs) # 리스트
  context = {'stu':qs[0]}
  return render(request, 'view.html', context)
  
  # qs = Student.objects.get(name = name) # 없을경우 에러
  # qs = get_object_or_404(Student, name = name) # 없을경우 구문리턴
  

# 학생리스트
def list(request):
  qs = Student.objects.all()
  context = {"slist":qs}
  # context 데이터를 html로 전달하는 변수
  return render(request, 'list.html',context)

# 학생 입력 페이지 호출
def write(request):
  if request.method == 'GET':
  # render : html 파일 호출
    print('GET방식으로 들어옴')
    return render(request, 'write.html')
  else:
    print('POST방식으로 들어옴')
    name = request.POST['name']
    major = request.POST['major']
    grade = request.POST['grade']
    age = request.POST['age']
    gender = request.POST['gender']
    print("입력데이터 : ",name,major,grade,age,gender)
    # DB 저장
    Student.objects.create(name=name, major=major, grade=grade, age=age, gender=gender)
    print("1명 학생 저장")
    return redirect("students:list")
    


# import redirect ; html에서 입력된 학생 정보 보내기
# # 학생입력저장
# def doWrite(request):
#   if request.method == 'POST':
#     name = request.POST['name']
#     major = request.POST['major']
#     grade = request.POST['grade']
#     age = request.POST['age']
#     gender = request.POST['gender']
#     print("입력데이터 : ",name,major,grade,age,gender)
#   else:
#     print('해당되는 데이터가 없습니다.')
#   return redirect("/")