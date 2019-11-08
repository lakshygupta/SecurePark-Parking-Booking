from django.db import models
from datetime import date
from datetime import datetime
# Create your models here.

GENDER_CHOICE = (
    ('male', 'Male'),
    ('female','Female'),
    ('others','Others'),
)

QUES_CHOICE = (
    ('book', 'What Is your favorite book?'),
    ('food', 'What is your favorite food?'),
    ('city', 'What city were you born in?'),
    ('place', 'Where is your favorite place to vacation?'),
)

VEHICLE_CHOICE = (
    ('two','Two Wheeler'),
    ('three','Three Wheeler'),
    ('four','Four Wheeler'),

)
class Registration(models.Model):
    mes_id = models.AutoField(primary_key=True)
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    email = models.EmailField(default="null")
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20,default="")
    passwordr = models.CharField(max_length=20,default="")
    addressfor = models.CharField(max_length=200,default="")
    contactnumber = models.CharField(max_length=10 ,default="")
    dob=models.DateField(default=date.today)
    gender=models.CharField(max_length=10 , choices=GENDER_CHOICE , default='male')
    ques = models.CharField(max_length=10, choices=QUES_CHOICE , default='book')
    answer = models.CharField(max_length=20,default="")

    def __str__(self):
        return self.fname

class Contact(models.Model):
    name = models.CharField(max_length=20)
    mail = models.CharField(max_length=200,default="null")
    contactno = models.CharField(max_length=10, default="")
    question = models.CharField(max_length=2000, default="")

    def __str__(self):
        return self.name


class Complaints(models.Model):
    fname = models.CharField(max_length=20)
    mname = models.CharField(max_length=20, default="")
    lname = models.CharField(max_length=20)
    contactno = models.CharField(max_length=10, default="")
    email = models.EmailField(default="null")
    address = models.CharField(max_length=200, default="")
    space = models.CharField(max_length=30, default="")
    message = models.CharField(max_length=2000, default="")

    def __str__(self):
        return self.fname

class Vehicleentry(models.Model):
    vnumber = models.CharField(max_length=10)
    vtype = models.CharField(max_length=10, choices=VEHICLE_CHOICE, default='two')
    contactno = models.CharField(max_length=10, default="")
    date = models.DateField(null=True, blank=True)
    intime = models.TimeField(null=True, blank=True)
    spacealloted = models.CharField(max_length=10)
    flooralloted = models.CharField(max_length=10)
    tagno = models.CharField(max_length=10)

    def __str__(self):
        return self.vnumber + '-' + self.vtype

class Vehicleexit(models.Model):
    vno = models.CharField(max_length=10,default='')
    vty = models.CharField(max_length=10, choices=VEHICLE_CHOICE, default='two')
    outtime = models.TimeField(null=True, blank=True)
    farem = models.CharField(max_length=4,null=True, blank=True)
    tno = models.CharField(max_length=10,default='')

    def __str__(self):
        return self.vno + '-' + self.vty


