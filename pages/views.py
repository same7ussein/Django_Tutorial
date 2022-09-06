from django.shortcuts import render
from .models import Login
from .forms import LoginForm
def index(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        data=Login(username=username,password=password)
        if data.is_valid:
            data.save()
    return render(request,'pages/index.html',{'lf':LoginForm})

def about(request):
    return render(request,'pages/about.html')