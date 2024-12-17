from audioop import error

from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import UserRegister
from django.http import HttpResponse

users = ['Vasia', 'Vitia', 'Gena']
info = {}

# Create your views here.

def sign_up_by_html(request):
    global info
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')
        if (username not in users) and (password == repeat_password) and int(age) > 18:
            return HttpResponse(f'Приветствуем, {username}!')
        if username in users:
            info = {'error': 'Пользователь уже существует'}
        if int(age) < 18:
            info = {'error': 'Вы должны быть старше 18'}
        if password != repeat_password:
            info = {'error': 'Пароли не совпадают'}
    return render(request, 'registration_page.html', context=info)



def sign_up_by_django(request):
    global info
    if request.method == "POST":
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            if (username not in users) and (password == repeat_password) and int(age) >18:
                return HttpResponse(f'Приветствуем, {username}!')
            if username in users:
                info = {'error': 'Пользователь уже существует'}
            elif int(age) < 18:
                info = {'error': 'Вы должны быть старше 18'}
            elif password != repeat_password:
                info = {'error': 'Пароли не совпадают'}
        else:
            form = UserRegister()

        return render(request, 'registration_page.html', context=info)



