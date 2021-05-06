from django.urls import path
from . import views
app_name = 'MyBlogs'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:Blog_id>/', views.detail, name='detail'),
    path('create', views.create, name='create'),
    path('success_saved', views.success_saved, name='success_saved'),
    path('<int:Blog_id>/update', views.Update.as_view(), name='update'),
    path('<int:Blog_id>/delete', views.Delete.as_view(), name='delete'),
]