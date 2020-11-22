from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date

# Create your models here.

class Hospital(models.Model):
    name      = models.CharField(max_length=50)
    phone     = models.CharField(max_length=15)
    emergency = models.CharField(max_length=15, blank=True)
    location  = models.CharField(max_length=100)
    email     = models.EmailField(max_length=100)

    def __str__(self):
        return self.name

class Doctor(models.Model):
    GENDER_CHOICES = (
        ('None', 'Select...'),
        ('Male', 'Male'),
        ('Female', 'Female'),
    )

    SPE_CHOICES = (
        ('None', 'Select...'),
        ('Medicine', 'Medicine'),
        ('Pediatric', 'Pediatric'),
        ('Obstetrics and Gynecolgy', 'Obstetrics and Gynecolgy'),
        ('Surgery', 'Surgery'),
        ('Ophthalmology', 'Ophthalmology'),
        ('Orthopedic', 'Orthopedic'),
        ('ENT "Ear ,Nose Throat"', 'ENT "Ear ,Nose Throat"'),
        ('Dermatology', 'Dermatology'),
    )

    user       = models.OneToOneField(User,null=True, blank=True, on_delete=models.CASCADE)
    picture    = models.ImageField(default="profiled.png", null=True, blank=True)
    firstname  = models.CharField(max_length=100)
    lastname   = models.CharField(max_length=100)
    gender     = models.CharField(max_length=10, choices=GENDER_CHOICES)
    speciality = models.CharField(max_length=100, blank=True, choices=SPE_CHOICES)
    phone      = models.CharField(max_length=15)
    workplace  = models.ForeignKey(Hospital, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.firstname + " " + self.lastname

    def drname(self):
        return self.firstname + " " + self.lastname

class Patient(models.Model):
    GENDER_CHOICES = (
        ('None', 'Select...'),
        ('Male', 'Male'),
        ('Female', 'Female'),
    )

    user           = models.OneToOneField(User,null=True, blank=True, on_delete=models.CASCADE)
    picture        = models.ImageField(default="profiled.png", null=True, blank=True)
    firstname      = models.CharField(max_length=100)
    lastname       = models.CharField(max_length=100)
    gender         = models.CharField(max_length=10, choices=GENDER_CHOICES)
    birthday       = models.DateField(null=True, blank=True)
    city           = models.CharField(max_length=20)
    address        = models.CharField(max_length=100)
    personal_phone = models.CharField(max_length=15, blank=False)
    relative_phone = models.CharField(max_length=15, blank=False)

    hospital       = models.ForeignKey(Hospital, null=True, blank=True, on_delete=models.CASCADE)
    doctor         = models.ForeignKey(Doctor, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.firstname + " " + self.lastname

    def calcAge(self):
        today = date.today()
        age   = today.year - self.birthday.year - ((today.month, today.day) < (self.birthday.month, self.birthday.day))
        return age

class MedicalRecord(models.Model):
    patient = models.OneToOneField(Patient,null=True, blank=True, on_delete=models.CASCADE)
    doctor  = models.ForeignKey(Doctor, null=True, blank=True,on_delete=models.CASCADE)
    report  = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.patient.firstname + " " + self.patient.lastname
