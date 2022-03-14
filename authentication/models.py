from django.db import models
from django.contrib.auth.models import User

# Create your models here.
GENDER_CHOICE = (
    ('male', 'Male'),
    ('female', 'Female'),
    ('others', 'Others'),
)
class Person(User):
	gender = models.CharField(choices= GENDER_CHOICE, max_length= 50)
	dob = models.DateField(auto_now= False, auto_now_add= False)
	country = models.CharField(max_length = 200)
	profile_pic = models.ImageField(upload_to= "proimage")