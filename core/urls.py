from django.urls import path
from django.contrib import admin
#from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', views.Register, name='register'),
    path('register/patient', views.registerPatient, name='registerPatient'),
    path('register/doctor', views.registerDoctor, name='registerDoctor'),

    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),

    path('editAccount/', views.editAccount, name='editAccount'),

    path('', views.home, name='home'),
    path('hospitals/', views.allHospitals, name='hospitals'),
    path('allpatientsdr/', views.allPatientsdr, name='patients'),
    path('alldoctors/', views.allDoctors, name='doctors'),
    path('drofpatient/', views.drofPatient, name='drofpatient'),
    path('patientmdr/', views.patientMdr, name='patientmdr'),

    path('ptaccount/', views.ptaccountSettings, name='ptaccount'),
    path('draccount/', views.draccountSettings, name='draccount'),

    path('drmedicalrecords/', views.drmedicalRecords, name='drmedicalrecords'),
    path('create_medical/', views.createMedical, name='createMedical'),
    path('edit_medical/<str:pk>/', views.editMedical, name='editMedical'),

    path('showemergency/', views.showEmergency, name='showemergency'),
    path('patientemergency/<str:pk>/', views.patientEmergency, name='patientemergency'),

    path('profilep_information/', views.profilePinformation, name='profilep_information'),
    path('profiled_information/', views.profileDinformation, name='profiled_information'),
]
