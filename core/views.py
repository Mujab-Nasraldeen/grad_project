from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse,Http404
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages
from django.urls import reverse

from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import Group

from .models import Patient, Doctor, Hospital, MedicalRecord
from .forms import CreateUserForm, LoginForm, PatientForm, DoctorForm, MedicalForm, MedicalUpdateForm, EditAccountForm
from .decorators import unauthenticated_user, allowed_users, admin_only


# Create your views here.

def Register(request):
    return render(request, 'register.html')

@unauthenticated_user
def registerPatient(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='patient')
            user.groups.add(group)
            Patient.objects.create(
                user=user,
                )

            messages.success(request, 'Account was created for ' + username)

            return redirect('login')


    context = {'form':form}
    return render(request, 'register_patient.html', context)

@unauthenticated_user
def registerDoctor(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='doctor')
            user.groups.add(group)
            Doctor.objects.create(
                user=user,
                )

            messages.success(request, 'Account was created for ' + username)

            return redirect('login')


    context = {'form':form}
    return render(request, 'register_doctor.html', context)

@unauthenticated_user
def loginPage(request):
    form = LoginForm()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        """
        if user.is_staff:
            login(request, user)
            return redirect('http://127.0.0.1:8000/admin/login/?next=/admin/')
        """

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, ' Username OR Password is incorrect')
        
    context = {'form':form}
    return render(request, 'login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def editAccount(request):
    form    = EditAccountForm(instance=request.user)
    if request.method == 'POST':
        form = EditAccountForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect(reverse('home'))
    
    context = {'form': form}
    return render(request, 'edit_account.html', context)

@login_required(login_url='login')
def home(request):
    hospitals      = Hospital.objects.all()
    hospital_count = hospitals.count()

    patients       = Patient.objects.all()
    patient_count  = patients.count()

    doctors        = Doctor.objects.all()
    doctor_count   = doctors.count()

    medicals       = MedicalRecord.objects.all()
    medical_count  = medicals.count()

    context        = {'hospital_count':hospital_count, 'patient_count':patient_count, 'doctor_count':doctor_count, 'medical_count':medical_count}
    return render(request, 'dashboard.html', context)

@login_required(login_url='login')
def allHospitals(request):
    hospitals      = Hospital.objects.all()
    context        = {'hospitals':hospitals}

    return render(request, 'allhospitals.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['doctor'])
def drmedicalRecords(request):
    MedicalRecords = MedicalRecord.objects.all()

    context        = {'MedicalRecords':MedicalRecords}
    return render(request, 'dr_medical.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['patient'])
def ptaccountSettings(request):
	patient = request.user.patient
	form = PatientForm(instance=patient)

	if request.method == 'POST':
		form = PatientForm(request.POST, request.FILES,instance=patient)
		if form.is_valid():
			form.save()


	context = {'form':form}
	return render(request, 'pt_account_settings.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['doctor'])
def draccountSettings(request):
	doctor = request.user.doctor
	form = DoctorForm(instance=doctor)

	if request.method == 'POST':
		form = DoctorForm(request.POST, request.FILES,instance=doctor)
		if form.is_valid():
			form.save()

	context = {'form':form}
	return render(request, 'dr_account_settings.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['doctor'])
def createMedical(request):
    form = MedicalForm()
    if request.method == 'POST':
        form = MedicalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('drmedicalrecords'))

    context = {'form':form}
    return render(request, 'create_medical.html', context)

@login_required(login_url='login')   
@allowed_users(allowed_roles=['doctor']) 
def editMedical(request, pk):
    medical = MedicalRecord.objects.get(id=pk)
    #print (medical.patient)
    form = MedicalUpdateForm(instance=medical)

    if request.method == 'POST':
        form = MedicalUpdateForm(request.POST, instance=medical)
        if form.is_valid():
            form.save()
            return redirect(reverse('drmedicalrecords'))

    context = {'form':form}
    return render(request, 'edit_medical.html', context)


@login_required(login_url='login')
def allDoctors(request):
    doctors = Doctor.objects.all()

    context   = {'doctors':doctors}
    return render(request, 'alldoctors.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['patient'])
def drofPatient(request):
 
    return render(request, 'drofpatient.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['doctor'])
def allPatients(request):
    ptsdr   = Patient.objects.filter(doctor=request.user.doctor)
    context = {'ptsdr':ptsdr}

    return render(request, 'drofpatient.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['doctor'])
def allPatientsdr(request):
    ptsdr   = Patient.objects.filter(doctor=request.user.doctor)
    context = {'ptsdr':ptsdr}

    return render(request, 'allpatients.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['patient'])
def patientMdr(request):
    ptmdr   = MedicalRecord.objects.filter(patient=request.user.patient)
    context = {'ptmdr':ptmdr}

    return render(request, 'patient_report.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['patient'])
def profilePinformation(request):

    return render(request, 'prf_patient.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['doctor'])
def profileDinformation(request):

    return render(request, 'prf_doctor.html')

@login_required(login_url='login')
@admin_only
def showEmergency(request):
    patients  = MedicalRecord.objects.all()

    context = {'patients':patients}
    return render(request, 'show_emrg.html', context)

def patientEmergency(request, pk):
    #ptmdr  = MedicalRecord.objects.get(id=pk)
    #ptmdr  = get_object_or_404(MedicalRecord, pk=pk)
    try:
        ptmdr = MedicalRecord.objects.get(id=pk)
    except MedicalRecord.DoesNotExist:
        raise Http404("Page Not Found 404")
   
    context = {'ptmdr':ptmdr}
    return render(request, 'patient_emrg.html', context)