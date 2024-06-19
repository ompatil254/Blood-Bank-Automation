from django.forms import ModelForm
from .models import Donor,DonationDrive
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']


class CreateAdminForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
          
class DonorForm(forms.ModelForm):
    class Meta:
        model = Donor
        fields = '__all__'
        exclude = ['unit_status', 'groups', 'profile_pic', 'RFID']

    SEX_CHOICES = [
        ('', 'Sex'),  # Placeholder option
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Transgender', 'Transgender'),
    ]
    BLOOD_GROUP_CHOICES = [
        ('', 'Blood Group'),  # Placeholder option
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ]

    Sex = forms.ChoiceField(choices=SEX_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    Bloodgroup = forms.ChoiceField(choices=BLOOD_GROUP_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))

class DonationDriveForm(ModelForm):
    class Meta:
        model=DonationDrive
        fields='__all__'
        exclude=['created_by']