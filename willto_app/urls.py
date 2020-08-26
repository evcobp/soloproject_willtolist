from django.urls import path, include
from django.conf.urls import url
from . import views


urlpatterns = [
    path('', views.login_page, name="login_page"),
    path('registration', views.registration, name="registration"),
    path('registration_page', views.registration_page, name="registration_page"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    path('success', views.success),
    path('create_user', views.create_user),
    path('task_list', views.task_list),
    path('task_questions', views.task_questions),
    path('new_task', views.new_task, name="new_task"),
    path('score', views.score),
    url(r'^save-session-data/$', views.save_session_data, name='save_session_data'),
    url(r'^access-session-data/$', views.access_session_data, name='access_session_data'),
    url(r'^delete-session-data/$', views.delete_session_data, name='delete_session_data'),
    url(r'^test-delete/$', views.test_delete, name='test_delete'),
    url(r'^test-session/$', views.test_session, name='test_session'),
]