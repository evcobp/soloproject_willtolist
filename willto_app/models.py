from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import re
import bcrypt

EMAIL_MATCH = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# Create your models here.
class UserManager(models.Manager):
    #Get User emails
    def get_all_username(self):
        return self.order_by('username')
    
    #New User Registration
    def register(self, postData):
        myhash = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt()).decode()
        User.objects.create(
            first_name= postData['first_name'],
            last_name= postData['last_name'],
            username= postData['username'],
            email= postData['email'],
            password= myhash
            )
        
    def authenticate(self, email):
        users_with_email = self.filter(email=email)
        if not users_with_email:
            return False
        user = users_with_email[0]
        return bcrypt.checkpw(password.encode(), user.password.encode())
        
    def basic_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 1:
            errors["first_name"] = "Field cannot be blank."
        if len(postData['last_name']) < 1:
            errors["last_name"] = "Field cannot be blank."
        return errors
            
    
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=45, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    confirm_password = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.username} {self.email}"
    
    objects = UserManager()
    
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
    score = models.IntegerField(default=0,('question_one'+'question_two'+'question_three'+'question_four'+'question_five'))
    
    def __str__(self):
        return f"{self.task_name} {self.notes} {self.score}"