from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import RegisterForm
from django.contrib.auth import login as auth_login, authenticate, login
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.views import LogoutView
from django.views import generic

class RegisterView(CreateView):
     form_class = UserCreationForm
     success_url = reverse_lazy('accounts:login')
     template_name = 'accounts_registration/signup.html'

# 회원가입 기능 구현
class SignupView(CreateView):
    model = User
    template_name = 'accounts_registration/signup.html'
    form_class = RegisterForm

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save()
        auth_login(self.request, user)
        return response

# 로그인 기능 구현
@login_required
def profile(request):
    return render(request, 'registration/profile.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect(request.GET.get('next') or 'accounts:profile')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts_registration/login.html', {'form': form})


# 로그아웃 기능 구현
class MyLogoutView(LogoutView):
    success_url = reverse_lazy('accounts:login')

logout = MyLogoutView.as_view()
