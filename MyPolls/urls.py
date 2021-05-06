from django.urls import path
from . import views
app_name = 'MyPolls'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('create_form', views.create_form, name='create_form'),
    path('create', views.create, name='create'),
    path('success_saved', views.success_saved, name='success_saved'),
    path('<int:question_id>/update', views.Update.as_view(), name='update'),
    path('<int:question_id>/delete', views.Delete.as_view(), name='delete'),
    path('<int:choice_id>/update_choice', views.ChoiceUpdateView.as_view(), name='update_choice'),
    path('create_choice', views.ChoiceCreateView, name='create_choice'),
    path('<int:choice_id>/delete_choice', views.ChoiceDeleteView.as_view(), name='delete_choice'),
]