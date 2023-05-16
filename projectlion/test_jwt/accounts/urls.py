from django.urls import path
from django.contrib.auth import views as auth_views
from .views import RegisterView
from . import views

app_name = 'accounts'

urlpatterns = [
	path('signup/', RegisterView.as_view(), name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]

