from django.urls import path, re_path
from . import views
from django.contrib.auth import views as auth_views

app_name='accounts'

urlpatterns=[
    path('signup/', views.SignupView, name='user_signup'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='user_login'),
    path('logout/', auth_views.LogoutView.as_view(), name='user_logout'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='accounts/password_change_form.html') , name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='accounts/password_change_done.html'), name='password_change_done'),
]
