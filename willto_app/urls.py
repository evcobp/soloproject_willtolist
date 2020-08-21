from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('loginpage', views.loginpage),
    path('registration', views.registration),
    path('login', views.login),
    path('logout', views.logout,),
    path('success', views.success),
    path('create_user', views.create_user),
    path('create_task', views.create_task),
    path('task_list', views.task_list),
    path('task_questions', views.task_questions),
    path('new_task', views.new_task),
    path('score', views.score),
]