from django.db import models
from django.contrib.auth.models import User,Group
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class RFIDTag(models.Model):
    RFID = models.CharField(max_length=30)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return self.RFID
    
class Donor(models.Model):
    STATUS_CHOICES = [
        ('Donated', 'Donated'),
        ('Tested and Processed', 'Tested and Processed'),
        ('Available for Transfusion', 'Available for Transfusion'),
        ('Utilized', 'Utilized'),
        ('Transferred to main bank','Transferred to main bank')
    ]
    SEX_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Transgender', 'Transgender'),
    ]
    BLOOD_GROUP_CHOICES = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ]
    groups = models.ManyToManyField(Group) 
    # user = models.ForeignKey(User, on_delete=models.CASCADE,default='John Doe') 
    Name = models.CharField(max_length=200, null=True)
    Age = models.PositiveIntegerField(
        validators=[
            MinValueValidator(18),
            MaxValueValidator(90)
        ])
    Sex = models.CharField(max_length=20, choices=SEX_CHOICES, null=True)
    Bloodgroup = models.CharField(max_length=3, choices=BLOOD_GROUP_CHOICES)

    Phone = models.CharField(max_length=15, null=True)
    Email = models.CharField(max_length=100, null=True)
    unit_status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Donated')
    RFID = models.ForeignKey(RFIDTag, on_delete=models.SET_NULL, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.Name


class DonationDrive(models.Model):
	Venue = models.CharField(max_length=200, null=True)
	Pincode = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	def __str__(self):
			return self.Venue


class DriveGroup(models.Model):
    drive = models.ForeignKey(DonationDrive, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.drive.Venue} - Group {self.pk}"

