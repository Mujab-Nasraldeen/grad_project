from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms

from .models import Patient, Doctor, Hospital, MedicalRecord

class LoginForm(forms.Form):
        username = forms.CharField(
            widget=forms.TextInput(
                attrs={
                    "placeholder" : "Username",                
                    "class": "form-control"
                }
            ))
        password = forms.CharField(
            widget=forms.PasswordInput(
                attrs={
                    "placeholder" : "Password",                
                    "class": "form-control"
                }
            ))

class CreateUserForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Username",                
                "class": "form-control"
            }
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder" : "Email",                
                "class": "form-control"
            }
        ))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Password",                
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Password Confirmation",                
                "class": "form-control"
            }
        ))
        
    class Meta:
        model  = User
        fields = ('username', 'email', 'password1', 'password2')
        

class EditAccountForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username','email')

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Username",                
                "class": "form-control"
            }
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder" : "Email",                
                "class": "form-control"
            }
        ))

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'
        exclude = ['user']
    
    picture = forms.ImageField(
        widget=forms.ClearableFileInput(
            attrs={              
                "class": "form-control-file",
                "id": "exampleFormControlFile1"
            }
        )
    )
    firstname = forms.CharField(
        required = True,
        widget=forms.TextInput(
            attrs={
                "placeholder" : "First Name",                
                "class": "form-control"
            }
        ))
    lastname = forms.CharField(
        required = True,
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Last Name",                
                "class": "form-control"
            }
        ))
    GENDER_CHOICES = (
        ('None', 'Select...'),
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    gender = forms.ChoiceField(
        required = True,
        widget=forms.Select(
            attrs={               
                "class": "form-control",
                "id": "exampleFormControlSelect1"
            }
        ), choices=GENDER_CHOICES)
    personal_phone = forms.CharField(
        required = True,
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Personal Phone Number",                
                "class": "form-control"
            }
        ))
    relative_phone = forms.CharField(
        required = True,
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Relative Phone Number",                
                "class": "form-control"
            }
        ))
    birthday = forms.DateField(
        required = True,
        widget=forms.DateInput(
            attrs={
                "type": "date",
                "class": "form-control"
            }
        ))
    city = forms.CharField(
        required = True,
        widget=forms.TextInput(
            attrs={
                "placeholder" : "City",                
                "class": "form-control"
            }
        ))
    address = forms.CharField(
        required = True,
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Address",                
                "class": "form-control"
            }
        ))
    hospital = forms.ModelChoiceField(
        queryset=Hospital.objects.all(),
        required = True,
        widget=forms.Select(
            attrs={               
                "class": "form-control",
            }
        ))
    doctor = forms.ModelChoiceField(
        queryset=Doctor.objects.all(),
        required = True,
        widget=forms.Select(
            attrs={               
                "class": "form-control",
            }
        ))

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'
        exclude = ['user']
    
    picture = forms.ImageField(
        widget=forms.ClearableFileInput(
            attrs={              
                "class": "form-control-file",
                "id": "exampleFormControlFile1"
            }
        )
    )
    firstname = forms.CharField(
        required = True,
        widget=forms.TextInput(
            attrs={
                "placeholder" : "First Name",                
                "class": "form-control"
            }
        ))
    lastname = forms.CharField(
        required = True,
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Last Name",                
                "class": "form-control"
            }
        ))
    GENDER_CHOICES = (
        ('None', 'Select...'),
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    gender = forms.ChoiceField(
        required = True,
        widget=forms.Select(
            attrs={               
                "class": "form-control",
                "id": "exampleFormControlSelect1"
            }
        ), choices=GENDER_CHOICES)
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
    speciality = forms.ChoiceField(
        required = True,
        widget=forms.Select(
            attrs={
                "placeholder" : "speciality",                
                "class": "form-control"
            }
        ), choices=SPE_CHOICES)
    phone = forms.CharField(
        required = True,
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Phone Number",                
                "class": "form-control"
            }
        ))
    workplace = forms.ModelChoiceField(
        queryset=Hospital.objects.all(),
        required = True,
        widget=forms.Select(
            attrs={               
                "class": "form-control",
            }
        ))

class MedicalForm(forms.ModelForm):
    class Meta:
        model  = MedicalRecord
        fields = '__all__'
    
    patient = forms.ModelChoiceField(
        queryset=Patient.objects.all(),
        required = True,
        widget=forms.Select(
            attrs={               
                "class": "form-control",
            }
        ))
    doctor = forms.ModelChoiceField(
        queryset=Doctor.objects.all(),
        required = True,
        widget=forms.Select(
            attrs={               
                "class": "form-control",
            }
        ))
    report = forms.CharField(
        required = True,
        widget=forms.Textarea(
            attrs={
                "placeholder" : "Please, Type Your Report Here...",                
                "class": "form-control"
            }
        ))

class MedicalUpdateForm(forms.ModelForm):
    class Meta:
        model  = MedicalRecord
        fields = '__all__'

    patient = forms.ModelChoiceField(
        queryset=Patient.objects.all(),
        required = True,
        disabled = True,
        widget=forms.Select(
            attrs={               
                "class": "form-control",
            }
        ))
    doctor = forms.ModelChoiceField(
        queryset=Doctor.objects.all(),
        required = True,
        widget=forms.Select(
            attrs={               
                "class": "form-control",
            }
        ))
    report = forms.CharField(
        required = True,
        widget=forms.Textarea(
            attrs={
                "placeholder" : "Please, Type Your Report Here...",                
                "class": "form-control"
            }
        ))
