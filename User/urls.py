from django.urls import path
from . import views

app_name = 'User'
urlpatterns = [
    path('', views.index, name='home'),
    path('login', views.Login.as_view(), name='login'),
    path('logout', views.Logout.as_view(), name='logout'),
    path('register', views.Register.as_view(), name='register'),
    path('success_saved', views.success_saved, name='success_saved')
]