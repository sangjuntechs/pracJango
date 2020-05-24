from django.shortcuts import render
from .models import User

def register(request) :
    if request.method == 'GET':
        return render(request,'register.html')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        

        user = User(
            username = username,
            password = password
        )

        user.save()

        return render(request, 'register.html')
        
