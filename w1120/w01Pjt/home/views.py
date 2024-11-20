from django.shortcuts import render

app_name = ''

def index(request):
  return render(request, 'index.html')
