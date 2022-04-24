from django.shortcuts import render
from django.shortcuts import render,redirect
from django.template import context
from django.contrib.auth.mixins import LoginRequiredMixin
from account.forms import RegisterForm,LoginForm, CustomPasswordChangeForm
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, PasswordChangeView



def register(request):
    if not request.user.is_authenticated:
        form = RegisterForm()
        if request.method == 'POST':
            form = RegisterForm(data=request.POST, files=request.FILES)
            if form.is_valid():
                user = form.save()
                user.set_password(form.cleaned_data['password'])
                user.save()
                return redirect('login')
        context = {
            'form': form
        }   
        return render(request,'register.html', context)
    else:
        return redirect('')


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = super().form_valid(form)
        form.instance.set_password(form.cleaned_data['password'])
        form.instance.save()
        return user


class ShopLoginView(LoginView):
    form_class = LoginForm
    template_name = 'login.html'




def login(request):
    form=LoginForm()
    next_page = request.GET.get('next', '/')
    if request.method=='POST':
       form = LoginForm(data=request.POST)
       if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                django_login(request, user)
                
                messages.add_message(request, messages.SUCCESS, 'Ugurla login oldunuz')
                return redirect(next_page)
            else:
                
                messages.add_message(request, messages.ERROR, 'Username ve ya password sehvdir!')
                
    context={
        'form':form
    }
    return render(request,'login.html',context)


@login_required
def user_profile(request):
    return render(request, 'user-profile.html')
    


@login_required
def logout(request):
    django_logout(request)
    return redirect('/login')


class ChangePasswordView(LoginRequiredMixin, PasswordChangeView):
    form_class = CustomPasswordChangeForm
    template_name = 'login.html'
    success_url = reverse_lazy('login')

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, 'Ugurla sifreniz deyisdi')
        return super().get_success_url()
