from django.urls import path
from . import views

from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('home/',views.home, name='home'),
    path('chan/',views.chan, name='chan'),
    path('sam/',views.sam, name='sam'),
    path('yao/',views.yao, name='yao'),
    path('done/',views.done, name='done'),
    path('',views.login, name='login'),
    path('signUp/',views.signUp, name='signUp'),
    

    

    path('useUser/', views.signUpForm, name='useUser'),
    path('addUser/', views.loginFrom, name='addUser'),
    path('logOut/', views.logOut, name='logOut')
    
]

