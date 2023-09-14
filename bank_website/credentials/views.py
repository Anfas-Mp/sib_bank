# Create your views here.
from django.contrib import messages,auth
from django.shortcuts import redirect,render
from django.contrib.auth.models import User

# Create your views here.



def register(request):
    if  request.method == 'POST':
        username=request.POST['UserName']
        firstname=request.POST['First_Name']
        lastname=request.POST['Last_Name']
        email=request.POST['Email']
        password=request.POST['Password']
        cpassword=request.POST['Password1']

        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username is already taken")
                return redirect('credentials:register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email is already taken")
                return redirect('credentials:register')
            else:
                user=User.objects.create_user(username=username,first_name=firstname,last_name=lastname,email=email,password=password)
                user.save();
                return redirect('credentials:login')
        else:
            messages.info(request,'incorrect password')
            return redirect('credentials:register')
        return redirect('/')
    return render(request,'register.html')

def login(request):
    if  request.method == 'POST':
        username=request.POST['UserName']
        password=request.POST['Password']
        user=auth.authenticate(username=username,password=password)
        
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'incorrect credentials')
            return redirect('credentials:login')

    return render(request,'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')