from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
import re
from app1.models import Url
re.compile('<title>(.*)</title>')

# Create your views here.
def Homepage(request):
    if request.method == 'POST':
        full_url = request.POST.get('full_url')
        obj = Url.create(full_url)
        print(obj.Shorturl)
        return render(request,'home.html',{
            'short_url' : request.get_host()+'/'+ obj.Shorturl,
            'full_url'  : obj.fullurl    })
    return render(request,'home.html')
def Signupage(request):
    if request.method=='POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        if pass1!=pass2:
            return HttpResponse('check password')

        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            #print(uname,email,pass1,pass2)
            return redirect('login')

        

        
        
    return render(request,'register.html')

def Loginpage(request):
    if request.method=='POST':
        uname = request.POST.get('username')
        pass1 = request.POST.get('password1')
        user = authenticate(request, username=uname,password = pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse('Username or password incorrect')


        #print(uname, pass1)
    return render (request,'login.html')

def redtourl(request,key):
    print(key)
    try:
        obj = Url.objects.get(Shorturl = key)
        print(obj)
        return redirect(obj.fullurl)
    except:
    
        return redirect(Homepage)
