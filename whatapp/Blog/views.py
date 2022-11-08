
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Blog,Blogs
from django.contrib.auth.models import User
from django.contrib import auth



from django.contrib.auth.decorators import login_required



# Create your views here.
@login_required(login_url='/')

def home(request):
    news = Blog.objects.all()
    return render(request,'Oudone.html',{
        'news':news
    })
        

def chan(request):
    two = Blogs.objects.all()
    return render(request,'Kongchan.html',{
        'two':two
    })
    
def sam(request):
    news = Blog.objects.all()
    return render(request,'Sam.html',{
        'news':news
    })

def yao(request):
    news = Blog.objects.all()
    return render(request,'Yao.html',{
        'news':news
    })

def done(request):
    news = Blog.objects.all()
    return render(request,'Done.html',{
        'news':news
    })

def login(request):
    return render(request, 'login.html')


def signUp(request):
    return render(request, 'signUp.html')


def loginFrom(request):
    username = request.POST['username']
    password = request.POST['password']

    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return redirect('/home')
    else:
        messages.error(request, 'Not Found :(')
        return redirect('/')

def signUpForm(request):
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['psw']
    re_password = request.POST['psw-repeat']
  
    if password == re_password:
        if User.objects.filter(username=username).exists():
            messages.info(request,'This username is already exist!')
            return redirect('singnUp/')
        elif User.objects.filter(password=password).exists():
            messages.info(request,'This password is already exist!')
            return redirect('singnUp/')
        else:
            new_user = User.objects.create_user(
                username = username,
                email = email,
                password = password,
                user_type = 2,
            )
            new_user.save()
            return redirect('/')
    else:
        messages.info(request,'This email is already exist!')
        return redirect('singnUp/')


def logOut(request):
    auth.logout(request)
    return redirect('/')