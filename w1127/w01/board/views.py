from django.shortcuts import render
from member.models import Member
from board.models import Board
from django.core.paginator import Paginator

# 게시글 적기
def bwrite(request):
  if request.method == "GET":
    return render(request, 'bwrite.html')
  else:
    id = request.session.get('session_id') # session_id의 id값을 가져옴.
    member = Member.objects.get(id=id)
    btitle = request.POST.get("btitle")
    bcontent = request.POST.get("bcontent")
    
    # DB 저장 - AutoField : 번호생성
    qs = Board.objects.create(member=member, btitle=btitle, bcontent=bcontent)
    qs.bgroup = qs.bno
    qs.save()
    
    context = {"wmsg":"1"}
    return render(request, "bwrite.html",context)

# 게시판리스트
def blist(request):
  npage = int(request.GET.get('npage',1)) # 넘어온 현재페이지
  qs = Board.objects.all().order_by("-bgroup","bstep")
  # 하단페이지처리 (넘버링)
  paginator = Paginator(qs,10)
  blist = paginator.get_page(npage) # 1페이지 10개
  
  context = {"blist":blist, 'npage':npage}
  return render(request, 'blist.html', context)
