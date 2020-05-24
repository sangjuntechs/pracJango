from django.shortcuts import render
from .models import User
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password

def register(request) :
    if request.method == 'GET':
        return render(request,'register.html')
    elif request.method == 'POST':
        username = request.POST.get('username',None)
        password = request.POST.get('password',None)
        password2 = request.POST.get('password2',None)

        res_data = {}
        if not (username and password and password2):
            res_data['error'] = '올바른 정보를 입력하세요.'
        if password != password2:
            res_data['error'] = '비밀번호가 틀립니다.'
        else:
            user = User(
                username = username,
                password = make_password(password)
            )

            user.save()

        return render(request, 'register.html', res_data)
            
        
