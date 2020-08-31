from django.urls import path, include, re_path
from . import views


urlpatterns = [
    path('',views.index),
    path('login_page', views.login_page, name="login_page"),
    path('registration', views.registration, name="registration"),
    path('registration_page', views.registration_page, name="registration_page"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    path('success', views.success),
    path('create_user', views.create_user),
    path('task_list_page', views.task_list_page, name="task_list_page"),
    path('task_list', views.task_list, name="task_list"),
    path('create', views.create, name="create"),
    path('create_task', views.create_task, name="create_task"),
    path('new_task', views.new_task, name='new_task'),
    re_path(r'^save-session-data/$', views.save_session_data, name='save_session_data'),
    re_path(r'^access-session-data/$', views.access_session_data, name='access_session_data'),
    re_path(r'^delete-session-data/$', views.delete_session_data, name='delete_session_data'),
    re_path(r'^test-delete/$', views.test_delete, name='test_delete'),
    re_path(r'^test-session/$', views.test_session, name='test_session'),
]