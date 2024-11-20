from django.shortcuts import render, redirect
from member.models import Member

def logout(request):
  # 세션 모두 삭제
  request.session.clear() # 세션 모두 삭제
  # del request.session['session_id'] # 해당 세션만 삭제
  return redirect('index')

def login(request):
  if request.method == 'GET':
    response = render(request, 'login.html')
  else:
    emsg = ""
    id = request.POST.get("id")
    pw = request.POST.get("pw")
    qs = Member.objects.filter(id=id,pw=pw)
    if qs:
      request.session['session_id'] = id
      request.session['session_nicName'] = qs[0].nicName
      context = {"emsg":emsg, "member":""}
      response = render(request, 'index.html', context)
    else:
      emsg = "아이디 또는 패스워드가 일치하지 않습니다."
      context = {"emsg":emsg, "member":""}
      response = render(request, 'login.html', context)
  return response
    

def cookDelete(request):
  if request.method == 'GET':
    response = render(request,'cookDelete.html')
    return response
  else:
    c = request.POST.get('ckey')
    response = render(request,'index.html')
    response.delete_cookie(c)
    print(c, "쿠키가 삭제되었습니다.")
  return response
    

def cookWrite(request):
  response = render(request, 'cookWrite.html')
  
  if request.method == 'GET':
    print("GET 방식으로 들어옴")
  else:
    response = render(request, 'index.html')
    print("POST 방식으로 들어옴")
    ckey = request.POST.get('ckey')
    cval = request.POST.get('cval')
    response.set_cookie(ckey,cval)
    
  return response
    
    
def mlist(request):
  return render(request, 'mlist.html')

