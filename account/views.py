from django.shortcuts import render
from django.shortcuts import render,redirect
from django.template import context
from account.forms import RegisterForm,LoginForm
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required



def register(request):
    form=RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            user = form.save()
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('/login')
        print(form)
    context={
        'form': form
    }
    return render(request,'register.html',context)


def login(request):
    form=LoginForm()
    next_page = request.GET.get('next', '/')
    if request.method=='POST':
       form = LoginForm(data=request.POST)
       if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                django_login(request, user)
                print('1')
                messages.add_message(request, messages.SUCCESS, 'Ugurla login oldunuz')
                return redirect(next_page)
            else:
                
                messages.add_message(request, messages.ERROR, 'Username ve ya password sehvdir!')
                print('2')
    context={
        'form':form
    }
    return render(request,'login.html',context)


# @login_required
# def user_profile(request):
#     return render(request, 'user-profile.html')
    


@login_required
def logout(request):
    django_logout(request)
    return redirect('/')