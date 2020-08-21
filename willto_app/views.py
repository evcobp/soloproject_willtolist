from django.shortcuts import render, redirect, HttpResponse
from .models import User, Task
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request, 'index.html')

def logout(request):
    request.session.clear()
    
    return redirect('/')

def loginpage(request):
    return render(request, 'login.html')


def registration(request):
    return render(request, 'registration.html')


def login(request):
    result = User.objects.authenticate('email')
    if result == False:
        messages.error(request, "Invalid Email or Password", extra_tags='login')
    else:
        user = User.objects.get(email=request.POST['email'])
        request.session['user_id'] = user.id
        return redirect('/success')
    return redirect('/login')


def success(request):
    return render(request, 'success.html')


def create_user(request):
    errors = User.objects.basic_validator(request.POST)
    if errors:
        for field,value in errors.items():
            messages.error(request, value, extra_tags='register')
        return redirect('/registration')
    else:
        user = User.objects.register(request.POST)
        return render(request, 'create_task.html')

            
def create_task(request, id):
    id = request.session['id']
    context = {
    Task.objects.create(task_name= request.POST['task_name'], due_date= request.POST['due_date'], notes= request.POST['notes'])
    }
    return render(request,'create_task', context)


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
    'question_nine':  request.POST.get('question_one'),
    'question_two': request.POST.get('question_two'),
    'question_three': request.POST.get('question_three'),
    'question_four': request.POST.get('question_four'),
    'question_five': request.POST.get('question_five')
    }
    
    return HttpResponse(context)

