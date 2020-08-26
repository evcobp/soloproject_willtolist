from django.shortcuts import render, redirect, HttpResponse
from .models import User, Task
from django.contrib import messages
import bcrypt

# Create your views here.
def login_page(request):
    context = {
        'users': User.objects.get_all_by_email()
    }
    return render(request, 'login_page.html', context)

def registration_page(request):
    context = {
        
    }
    return render(request, 'registration_page.html', context)

def registration(request):
    errors = User.objects.validate(request.POST)
    if errors:
        for field, value in errors.itmes():
            messages.error(request, value, extra_tags='register')
        return redirect('/registration_page')
    new_user = User.objects.register(request.POST)
    request.session['user_id'] = new_user.id
    messages.success(request, "You have successfully registered, please login.", extra_tags='signin')
    return redirect('/')


def login(request):
    result = User.objects.authenticate(request.POST['email'], request.POST['password'])
    if result == False:
            messages.error(request, "Invalid Email or Password", extra_tags='log_in')

    else:
        user = User.objects.get(email=request.POST['email'])
        request.session['user_id'] = user.id
        messages.success(request, "You've successfully logged in!", extra_tags='success')
        return redirect('/task_list')
    return redirect('/')

def logout(request):
    messages.success(request, "You have successfully logged out", extra_tags='logout')
    request.session.clear()
    return redirect('/')

def success(request):
    return render(request, 'success.html')


def create_user(request):
    errors = User.objects.basic_validator(request.POST)
    if errors:
        for field, value in errors.items():
            messages.error(request, value, extra_tags='register')
        return redirect('/registration')
    else:
        id = User.objects.register(request.POST['id'])
        return render(request, 'task_list.html')

            
def create_task(request):
    context = {
        Task.objects.create(
            task_name= request.POST['task_name'], 
            due_date= request.POST['due_date'], 
            notes= request.POST['notes'],
            question_one=request.POST['question_one'],
            question_two=request.POST['question_two'],
            question_three=request.POST['question_three'],
            question_four=request.POST['question_four'],
            question_five=request.POST['question_five']
        )}
    return render(request,'task_list.html', context)


def delete_task(request):
    pass

    
def new_task(request):
    return render(request,'new_task.html')


def task_list(request):
    context = {
        "all_tasks": Task.objects.all()
    }
    return render(request,'task_list.html', context)


def task_questions(request):
    active_task= Task.objects.last()
    context = {
        'show_task': active_task.task_name,
        'show_due_date': active_task.due_date,
        'show_notes': active_task.notes
    }
    return render(request,'task_questions.html', context)


def score(request):
    context = {
        request.POST.get('question_one')+request.POST.get('question_two')+request.POST.get('question_three')+request.POST.get('question_four')+request.POST.get('question_five')
    }
    return HttpResponse(context)


def stop_tracking(request):
    pass


def test_session(request):
    request.session.set_test_cookie()
    return HttpResponse("Testing session cookie")


def test_delete(request):
    if request.session.test_cookie_worked():
        request.session.delete_test_cookie()
        response= HttpResponse("Cookie test passed")
    else: 
        response= HttpResponse("Cookie test failed")
    return response


def save_session_data(request):
    # set new data
    request.session['id'] = 1
    request.session['name'] = 'root'
    request.session['password'] = 'rootpass'
    return HttpResponse("Session Data Saved")


def access_session_data(request):
    response = ""
    if request.session.get('id'):
        response += "Id : {0} <br>".format(request.session.get('id'))
    if request.session.get('name'):
        response += "Name : {0} <br>".format(request.session.get('name'))
    if request.session.get('password'):
        response += "Password : {0} <br>".format(request.session.get('password'))

    if not response:
        return HttpResponse("No session data")
    else:
        return HttpResponse(response)


def delete_session_data(request):
    try:
        del request.session['id']
        del request.session['name']
        del request.session['password']
    except KeyError:
        pass

    return HttpResponse("Session Data cleared")