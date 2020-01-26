from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
#from ..forms import UserForm
from ..models import User
from ..admin import UserCreationForm,UserCreationForm2
from time import sleep

def decidir_usuario(request):
    return render(request, 'usuarios/cadastro_usuario.html')

def sucesso_usuario(request):
    return render(request, 'usuarios/sucesso.html')

def cadastarar_servidor(request):
    mensagem = ""
    sucesso = ""
    if request.method == "POST":
        form_usuario = UserCreationForm2(request.POST)

        if form_usuario.is_valid():
            form_usuario.save()
            sucesso = "ok"


        else:
            mensagem = form_usuario.errors
    else:
        form_usuario = UserCreationForm2()

    return render(request, 'usuarios/form_cadastro_servidor.html',
                  {"form_usuario": form_usuario, 'mensagem': mensagem,'sucesso':sucesso})

def cadastarar_aluno(request):
    mensagem = ""
    sucesso=""
    if request.method == "POST":
        form_usuario = UserCreationForm(request.POST)


        if form_usuario.is_valid():
            #matricula=form_usuario.cleaned_data['registro']
            form_usuario.save()
            sucesso="ok"
            #return redirect('sucesso_usuario')
        else:
            mensagem=form_usuario.errors
    else:
        form_usuario = UserCreationForm()
    print(mensagem)
    return render(request, 'usuarios/form_cadastro_aluno.html',
                  {"form_usuario": form_usuario,'mensagem':mensagem,'sucesso':sucesso})

def logar_usuario(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        usuario = authenticate(request, username=username,password=password)
        if usuario is not None:
            login(request,usuario)
            return redirect('calendario')
        else:
            messages.error(request,"Usuario ou senha incoretos")
            return redirect('logar_usuario')
    else:
        form_login = AuthenticationForm()
    return render(request,'usuarios/form_login.html',{"form_login":form_login})
def deslogar_usuario(request):
    logout(request)
    return redirect('logar_usuario')