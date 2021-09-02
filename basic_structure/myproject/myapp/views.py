from django.shortcuts import render, redirect
from django.http import HttpResponse
from myapp.models import details
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.

def apprun(request):
    return render(request,'myapp/index.html')


# def display_user(request):

#     data_len = len(details.objects.all())
#     obj_list = []
#     # print(data_len)
#     for i in range(1,data_len+1):
#         obj = details.objects.get(id=i)
#         obj_list.append(obj)
        
   
#     params = {
#         'obj' : obj_list,
        
#     }

#     return render(request,'myapp/display.html',params)

            # or

def display_user(request):

    obj = details.objects.all()
        
   
    params = {
        'obj' : obj,
        
    }

    return render(request,'myapp/display.html',params)



def app_form(request):
    if request.POST:
        name = request.POST.get('nm')
        # print(name)
        age = request.POST.get('age')
        mark = request.POST.get('mk')

        details.objects.create(name=name,age=age,marks=mark)
        return render(request,'myapp/form.html')
    
    return render(request,'myapp/form.html')



def register(request):

    if request.method == 'POST':
        username = request.POST['uname']
        email = request.POST['em']
        password1 = request.POST['pass1']
        password2 = request.POST['pass2']
        
        if password1 == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Used')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Already Used')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Password are Not same')
            return redirect('register')
        
    else:

        return render(request, 'myapp/register.html')



def login(request):

    if request.method == 'POST':
        username = request.POST['uname']
        password = request.POST['pass']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('login')
    else:
        return render(request,'myapp/login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def post(request,pk):
    return render(request,'myapp/post.html',{'pk':pk})