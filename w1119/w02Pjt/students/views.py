from django.shortcuts import render,redirect
from students.models import Student

def write(request):
  if request.method == 'POST':
    name = request.POST.get('name')
    major = request.POST.get('major')
    grade = request.POST.get('grade')
    age = request.POST.get('age')
    gender = request.POST.get('gender')
    hobbys = request.POST.getlist('hobby')
    hobby = ', '.join(hobbys)
    
    Student.objects.create(name=name,major=major,grade=grade,age=age,gender=gender,hobby=hobby)
    return redirect('/students/list/')
  else:
    return render(request, 'write.html')
  
def list(request):
  qs = Student.objects.all()
  contents = {'slist':qs}
  return render(request, 'list.html', contents)
