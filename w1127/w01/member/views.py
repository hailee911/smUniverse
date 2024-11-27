from django.shortcuts import render,redirect
from member.models import Member

# 가족등록
def reg(request):
  if request.method == "GET":
    return render(request, 'reg.html')
  else:
    id = request.POST.get('id')
    pw = request.POST.get('pw')
    name = request.POST.get('name')
    age = request.POST.get('age')
    role = request.POST.get('role')
    qs = Member(id=id,pw=pw,name=name,age=age,role=role)
    qs.save()
    return redirect("/")
  
# 로그인
def login(request):
  if request.method == "GET":
    return render(request, 'login.html')
  else:
    id = request.POST.get('id')
    pw = request.POST.get('pw')
    qs = Member.objects.filter(id=id, pw=pw)
    if qs:
      msg = "로그인 되었습니다."
      print(msg)
      # 세션 연결
      request.session['session_id'] = id
      request.session['session_role'] = qs[0].role
      print(qs[0].role)
      return redirect('index')
    else:
      msg = "아이디 또는 패스워드가 일치하지 않습니다."
      print(msg)
      return render(request,'login.html',{"login_msg":msg})

# 로그아웃
def logout(request):
  request.session.clear() # 전체 세션 삭제
  # del request.session['session_id'] 해당 세션 삭제
  return redirect("/")