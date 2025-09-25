from django.shortcuts import render
from django.http.response import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = User.objects.filter(username=username).first()

        if user:
            return render(request, 'erro_cadastro.html')
        
        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()

        #para definir administradores:
        #user = User.objects.create_user(username=username, email=email, password=senha)
        return render(request, 'homepage.html')

def login_view(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password=senha)
        print(user)
        if user:
            login(request, user)
            return render(request, 'homepage.html')
        else:
            return render(request, 'erro_login.html')

@login_required(login_url='/auth/login') #esse comando impossibilita a entrada de usuários na homepage na qual os mesmo não possua login      
def restrito_view(request):
    return render(request, 'homepage.html')
