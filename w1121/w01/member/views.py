from django.shortcuts import render, redirect
from member.models import Member


# 회원정보삭제
def mdelete(request,id):
  print("회원정보 : ",id)
  Member.objects.get(id=id).delete()
  return redirect("member:mlist")
  

# 회원정보수정
def mupdate(request,id):
  if request.method == 'GET':
    qs = Member.objects.filter(id=id)
    context = {"mem":qs[0]}
    return render(request,'mupdate.html', context)
  else:
    id = request.session['session_id'] # admin이 아니면 세션을 가지고 저장
    ## 관리자 로그인이면 id를 가져와서 저장
    if request.session['session_id'] == 'admin':
      id = request.POST.get("id")
    pw = request.POST.get("pw")
    name = request.POST.get("name")
    nicname = request.POST.get("nicname")
    tel = request.POST.get("tel")
    gender = request.POST.get("gender")
    hobbys = request.POST.getlist('hobby')
    hobby = ','.join(hobbys)
    qs = Member.objects.get(id=id)
    qs.pw = pw
    qs.name = name
    qs.nicname = nicname
    qs.tel = tel
    qs.gender = gender
    qs.hobby = hobby
    qs.save()
    return redirect("member:mlist")


def mwrite(request):
  if request.method == "GET":
    return render(request,'mwrite.html')
  else:
    id = request.POST.get('id')
    pw = request.POST.get('pw')
    name = request.POST.get('name')
    nicname = request.POST.get('nicname')
    tel = request.POST.get('tel')
    gender = request.POST.get('gender')
    hobbys = request.POST.getlist('hobby')
    hobby = ','.join(hobbys)
    qs = Member(id=id,pw=pw,name=name,nicname=nicname,tel=tel,gender=gender,hobby=hobby)
    qs.save()
    return redirect("member:mlist")


# 회원상세
def mview(request,id):
  print('아이디',id)
  qs = Member.objects.filter(id=id)
  context = {"mem":qs[0]}
  return render(request, 'mview.html',context)

# 회원리스트
def mlist(request):
  id = request.session['session_id']
  if id == 'admin':
    qs = Member.objects.all()
  else:
    qs = Member.objects.filter(id=id)
  context = {"mlist":qs}
  return render(request, 'list.html',context)
  
    
# 로그아웃
def logout(request):
  request.session.clear() # 전체 세션 삭제
  # del request.session['session_id'] 해당 세션 삭제
  return redirect("/")

# 로그인 페이지(if), 로그인 버튼(else)
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
      request.session['session_nicname'] = qs[0].nicname
      return redirect('index')
    else:
      msg = "아이디 또는 패스워드가 일치하지 않습니다."
      print(msg)
      return render(request,'login.html',{"login_msg":msg})
  
