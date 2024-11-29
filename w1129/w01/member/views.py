from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers #json타입
from member.models import Member

# 회원가입 03
def step03(request):
  return render(request,'step03.html')

# 로그인
def login(request):
  return render(request, 'login.html')

# 로그아웃
def logout(request):
  request.session.clear() # 모두삭제 , del request.session['session_id'] - 1개 삭제
  context = {"outmsg":"1"}
  return render(request, 'index.html', context)

# json 타입 변경 - list,dic타입 qs : set -> list타입변경
# 로그인 체크
# @csrf_exempt :: 예외처리
def loginChk(request):
  id = request.POST.get("id","")
  pw = request.POST.get("pw","")
  qs = Member.objects.filter(id=id,pw=pw)
  print("확인 : ",id,pw)
  if qs:
    print("성공")
    request.session['session_id'] = id
    request.session['session_nicName'] = qs[0].nicName
    list_qs = list(qs.values())
    context = {"result":"success","member":list_qs}
  else:
    print("실패")
    context = {"result":"fail"}
    
  return JsonResponse(context)

def idChk(request):
  id = request.GET.get("id","")
  qs = Member.objects.filter(id=id)
  if qs:
    print(qs)
    context = {"result":"success"}
  else:
    context = {"result":"fail"}
    
  return JsonResponse(context)