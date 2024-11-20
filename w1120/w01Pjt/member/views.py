from django.shortcuts import render
from member.models import Member

# 로그인페이지
# 쿠키정보 검색 : request.COOKIES.get('이름')
# 쿠키 저장 : response.set_cookie('key','value')
# 쿠키 삭제 : response.delete_cookie('key')
def login(request):
  if request.method == 'GET':
    print("쿠키정보 : ",request.COOKIES)
    print("cookinfo 쿠키정보 : ",request.COOKIES.get('cookinfo'))
    saveId = request.COOKIES.get('saveId','')
    context = {"saveId":saveId}
    response = render(request,'login.html',context)
    # 쿠키 설정(저장)
    # max_age가 없으면 브라우저 종료시 삭제, max_age=60초*60분 후 삭제 1달 = 60초*60분*24시간*30일
    ## 쿠키정보 검색
    if not request.COOKIES.get('cookinfo'):
      response.set_cookie('cookinfo','1111',max_age=60*60)
    return response
  else:
    print("쿠키정보 : ", request.COOKIES)
    id = request.POST.get("id")
    pw = request.POST.get("pw")
    saveId = request.POST.get("saveId") # 1 / 값없음
    print("전달받은 정보 : ",id,pw,saveId)
    response = render(request,'login.html')
    # 아이디 기억하기 정보가 있으면
    if saveId is not None:
      response.set_cookie('saveId',id, max_age=60*60) # 아이디기억하기 체크가 있으면 쿠키 저장
    else:
      response.delete_cookie('saveId') # 아이디기억하기 체크가 없으면 쿠키 삭제
    return response

# 회원전체리스트 페이지
def mlist(request):
  qs = Member.objects.all()
  context = {'mlist':qs}
  return render(request, 'mlist.html',context)

def login2(request):
  if request.method == "GET":
    cookId = request.COOKIES.get('cookId','')
    context = {"cookId": cookId}
    return render(request,'login2.html',context)
  
  else:
    response = render(request,'index.html')
    # 3개정보
    id = request.POST.get('id')
    pw = request.POST.get('pw')
    saveId = request.POST.get('saveId')
    if saveId is not None:
      response.set_cookie('cookId',id,max_age=60*60)
    else:
      response.delete_cookie('cookId')
    
    return response
  
def product(request):
  if request.method == "GET":
    pId = request.COOKIES.get('pId','')
    pName = request.COOKIES.get('pName','')
    pOption = request.COOKIES.get('pOption','')
    context = {"pId": pId,"pName":pName, "pOption":pOption}
    return render(request,'product.html',context)
  else:
    response = render(request,'index.html')
    # 3개정보
    pId = request.POST.get('pId')
    pName = request.POST.get('pName')
    pOption = request.POST.get('pOption')
    saveProduct = request.POST.get("saveProduct")
    if saveProduct is not None:
      # print("쿠키정보 : ",pId,pOption)
      response.set_cookie('pId',pId,max_age=60*60)
      response.set_cookie('pName',pName,max_age=60*60)
      response.set_cookie('pOption',pOption,max_age=60*60)
    else:
      response.delete_cookie('pId')
      response.delete_cookie('pName')
      response.delete_cookie('pOption')
    
    return response