from django.db import models

class Member(models.Model):
    m_id = models.AutoField(primary_key=True)
    f_name = models.CharField("Όνομα", max_length=50)
    l_name = models.CharField("Επίθετο", max_length=50)
    email = models.EmailField("Email", unique=True, blank=True)
    phone = models.CharField("Τηλέφωνο", max_length=10)
    age = models.IntegerField("Ηλικία", max_length=2)
    address = models.TextField("Διεύθυνση", blank=True)
    registration_date = models.DateField(auto_now_add=True)

class Employee(models.Model):
    e_id = models.AutoField(primary_key=True)
    f_name = models.CharField("Όνομα", max_length=50)
    l_name = models.CharField("Επίθετο", max_length=50)
    email = models.EmailField("Email")
    phone = models.CharField("Τηλέφωνο", max_length=10)
    age = models.IntegerField("Ηλικία", max_length=2)
    hire_date = models.DateField("Ημερομηνία Πρόσληψης", auto_now_add=True)

class Trainer(Employee):
    specialty = models.CharField("Ειδικότητα", max_length=100)
    certifications = models.TextField("Πιστοποιήσεις")

class Secretary(Employee):

class Class(models.Model):
    c_id = models.AutoField(primary_key=True)
    name = models.TextField("Όνομα Προγράμματος", max_length=100)
    description = models.TextField
    capacity = 
    date = 

class Subscription(models.Model):
    s_id = models.AutoField(primary_key=True)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    participations = models.IntegerField ("Συμμετοχές")