from django.shortcuts import render, redirect, HttpResponse
from willto_app.models import User, Task
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
        for field, value in errors.items():
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
        return redirect('/task_list_page')
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

            

def create(request, task_form):
    return Task.objects.create(
        task_name=task_form['task_name'],
        due_date=task_form['due_date'],
        notes=task_form['notes'],
        question_one=task_form['question_one'],
        question_two=task_form['question_two'],
        question_three=task_form['question_three'],
        question_four=task_form['question_four'],
        question_five=task_form['question_five'],
    )
    def score(request):
        questions = [Task.question_one, Task.question_two, Task.question_three,
                    Task.question_four, Task.question_five]
        for question in questions:
            score = sum(questions[0:4])
            return score
        
    def update_score(request):
        thistask = self.create_task
        task_score = thistask.score
        task_score.save()
            

def create_task(request):
    pass


def delete_task(request):
    pass



def task_list_page(request):
    context = {
        "all_tasks": Task.objects.all()
    }
    return render(request,'task_list.html', context)



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