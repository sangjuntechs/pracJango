from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from .models import User
def home(request):
    user_id = request.session.get('user')

    if user_id:
        user = User.objects.get(pk=user_id)
        return HttpResponse(user.username+" 님 반갑습니다.")
       
    return HttpResponse('홈페이지')

def logout(request):
    if request.session.get('user'):
        del(request.session['user'])

    return redirect('/')

    


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method =='POST':
        username = request.POST.get('username',None)
        password = request.POST.get('password',None)
        
        res_data={}
        if not (username and password):
            res_data['error'] = '올바른 정보를 입력하세요.'
        else:
            user = User.objects.get(username=username)
            if check_password(password, user.password):
                request.session['user'] = user.id
                return redirect ('/')
            else:
                res_data['error'] = '비밀번호가 틀렸습니다.'
    return render(request, 'login.html',res_data)


def register(request) :
    if request.method == 'GET':
        return render(request,'register.html')
    elif request.method == 'POST':
        username = request.POST.get('username',None)
        useremail = request.POST.get('useremail',None)
        password = request.POST.get('password',None)
        password2 = request.POST.get('password2',None)
        

        res_data = {}
        
        if not (username and password and password2 and useremail):
            res_data['error'] = '올바른 정보를 입력하세요.'
        elif password != password2:
            res_data['error'] = '비밀번호가 틀립니다.'
        
        #elif User.objects.get(username=username):
            #res_data['error'] = '이미 등록된 사용자입니다.'
            
        else:
            user = User(
                username = username,
                useremail = useremail,
                password = make_password(password)
                    
            )

            user.save()
           

        return render(request,'register.html',res_data)
            
        
