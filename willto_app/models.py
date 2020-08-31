from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.datastructures import MultiValueDictKeyError
import datetime
from datetime import date
import re
import bcrypt

EMAIL_MATCH = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# Create your models here.
class UserManager(models.Manager):
    #Get User emails
    def get_all_by_email(self):
        return self.order_by('email')
    
    #New User Registration
    def register(self, form_data):
        myhash = bcrypt.hashpw(form_data['password'].encode(), bcrypt.gensalt()).decode()
        return self.create(
            first_name= form_data['first_name'],
            last_name= form_data['last_name'],
            username= form_data['username'],
            email= form_data['email'],
            password= myhash
            )
        
    def authenticate(self, email, password):
        users_with_email = self.filter(email=email)
        if not users_with_email:
            return False
        user = users_with_email[0]
        return bcrypt.checkpw(password.encode(), user.password.encode())
        
    def validate(self, form_data):
        
        errors = {}
        if len(form_data['first_name']) < 1:
            errors["first_name"] = "Field cannot be blank."
        if len(form_data['last_name']) < 1:
            errors["last_name"] = "Field cannot be blank."
        if len(form_data['email']) < 1:
            errors["email"] = "Email cannot be blank."
        if not EMAIL_MATCH.match(form_data['email']):
            errors['email'] = "Invalid Email."
        if form_data['password'] != form_data['confirm_password']:
            errors['password'] = "Passwords do not match"
        
        users_with_email = self.filter(email=form_data['email'])
        if users_with_email:
            errors['email'] = "Email already in use."
        
        return errors
             
        
        
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=45, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    confirm_password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    objects = UserManager()
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.username} {self.email}"

        
class Task(models.Model):
    task_name = models.TextField()
    due_date = models.DateTimeField()
    notes = models.TextField()
    user = models.ForeignKey(User,related_name="tasks",default="no_user",on_delete=models.CASCADE)
    question_one = models.IntegerField(default = 1, validators=[MaxValueValidator(10), MinValueValidator(1)])
    question_two = models.IntegerField(default = 1, validators=[MaxValueValidator(10), MinValueValidator(1)])
    question_three = models.IntegerField(default = 1, validators=[MaxValueValidator(10), MinValueValidator(1)])
    question_four = models.IntegerField(default = 1, validators=[MaxValueValidator(10), MinValueValidator(1)])
    question_five = models.IntegerField(default = 1, validators=[MaxValueValidator(10), MinValueValidator(1)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.task_name} {self.notes} {self.score}"