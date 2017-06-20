from django.db import models

# Create your models here.
from django.db import models
from django.core.urlresolvers import reverse


class Staff(models.Model):
    STATUS_CHOICES = (
        ('Manager', 'Manager'), ('Reviewer', 'Reviewer'),
        ('Processor', 'Processor'),
    )
    StaffId = models.CharField("Staff ID",max_length=20, primary_key= True)
    FirstName = models.CharField("First Name", max_length=50)
    LastName = models.CharField("Last Name", max_length=50)
    StaffRole = models.CharField("Role",max_length=50, choices=STATUS_CHOICES, default="")
    Susername = models.CharField("UserName",max_length=50)
    Spassword = models.CharField("Password",max_length=50)
    def __str__(self):
        return self.FirstName+" "+ self.LastName

#    def get_absolute_url(self):
#        return reverse ('index')

    class Meta:
        managed = False
        db_table = 'Staff'
        app_label = 'website'

class Provider(models.Model):
    STATUS_CHOICES = (
        ('PrimaryCare', 'PrimaryCare'), ('EmergencyCare', 'EmergencyCare'),
        ('Hospital', 'Hospital'), ('Others', 'Others'),
    )
    STATUS_CHOICES1 = (
        ('HMO', 'HMO'), ('PPO', 'PPO'),
    )

    State_choice = (('Alabama', 'Alabama'), ('Alaska', 'Alaska'), ('Arizona', 'Arizona'), ('Arkansas', 'Arkansas'),
                    ('California', 'California'), ('Colorado', 'Colorado'), ('Connecticut', 'Connecticut'),
                    ('Delaware', 'Delaware'),
                    ('District of Columbia', 'District of Columbia'),
                    ('Florida', 'Florida'), ('Georgia', 'Georgia'), ('Hawaii', 'Hawaii'), ('Idaho', 'Idaho'),
                    ('Illinois', 'Illinois'),
                    ('Indiana', 'Indiana'), ('Iowa', 'Iowa'), ('Kansas', 'Kansas'), ('Kentucky', 'Kentucky'),
                    ('Louisiana', 'Louisiana'),
                    ('Maine', 'Maine'), ('Maryland', 'Maryland'), ('Massachusetts', 'Massachusetts'),
                    ('Michigan', 'Michigan'),
                    ('Minnesota', 'Minnesota'), ('Mississippi', 'Mississippi'), ('Missouri', 'Missouri'),
                    ('Montana', 'Montana'),
                    ('Nebraska', 'Nebraska'), ('Nevada', 'Nevada'), ('New Hampshire', 'New Hampshire'),
                    ('New Jersey', 'New Jersey'),
                    ('New Mexico', 'New Mexico'), ('New York', 'New York'), ('North Carolina', 'North Carolina'),
                    ('North Dakota', 'North Dakota'), ('Ohio', 'Ohio'), ('Oklahoma', 'Oklahoma'), ('Oregon', 'Oregon'),
                    ('Pennsylvania', 'Pennsylvania'),
                    ('Rhode Island', 'Rhode Island'), ('South Carolina', 'South Carolina'),
                    ('South Dakota', 'South Dakota'),
                    ('Tennessee', 'Tennessee'), ('Texas', 'Texas'), ('Utah', 'Utah'), ('Vermont', 'Vermont'),
                    ('Virginia', 'Virginia'),
                    ('Washington', 'Washington'), ('West Virginia', 'West Virginia'), ('Wisconsin', 'Wisconsin'),
                    ('Wyoming', 'Wyoming'),)

    ProviderID = models.CharField("Provider ID", max_length=20, primary_key = True)
    ProviderName = models.CharField("Provider Name", max_length=50)
    ProviderType = models.CharField("Network Type", max_length=50, choices=STATUS_CHOICES, default="")
    NetworkType = models.CharField("Provider(HMO/PPO)", max_length=50, choices=STATUS_CHOICES1, default="")
    ProviderAddress = models.CharField("Address Line 1", max_length=50)
    City = models.CharField(max_length=50)
    ProviderState = models.CharField("State", max_length=50 , choices=State_choice, default="")
    ZipCode = models.IntegerField("Zip Code", default=0)
    PhoneNumber = models.IntegerField("Office Phone", default=0)

    def __str__(self):
        return self.ProviderName+" "+ self.ProviderType

#    def get_absolute_url(self):
#        return reverse ('index')

    class Meta:
        managed = False
        db_table = 'Provider'
        app_label = 'website'

class Service(models.Model):
    ServiceTypeId = models.CharField(max_length=10, primary_key = True)
    TypeName =  models.CharField(max_length=50)
    ServiceCategory = models.CharField(max_length=50)


class Patient(models.Model):
    PatientID = models.CharField(max_length=20, primary_key=True)
    FirstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    Gender = models.CharField(max_length=50)
    PatientAddress = models.CharField(max_length=50)
    City = models.CharField(max_length=50)
    PatientState = models.CharField(max_length=50)
    ZipCode = models.IntegerField(default=0)
    PhoneNumber = models.IntegerField(default=0)
    DateOfBirth = models.DateTimeField()
    Employment = models.BooleanField(default = True)
    Age = models.IntegerField(default=0)

    def __str__(self):
        return self.FirstName+" "+ self.LastName

#    def get_absolute_url(self):
#        return reverse ('index')

    class Meta:
        managed = False
        db_table = 'Patient'
        app_label = 'website'


class Policy(models.Model):
    PolicyId = models.CharField(max_length=20, primary_key=True)
    PolicyName = models.CharField(max_length=50)
    PolicyDuration = models.IntegerField(default=0)
    PolicyType = models.CharField(max_length=50)
    PatientId = models.ForeignKey(Patient, on_delete=models.CASCADE)

class ReasonForDenial(models.Model):
    ReasonID = models.CharField(max_length=20, primary_key=True)
    ReasonDescription = models.CharField(max_length=200)

    def __str__(self):
        return self.ReasonDescription
    class Meta:
        managed = False
        db_table = 'ReasonForDenial'
        app_label = 'website'


class Claim(models.Model):
    ClaimID = models.CharField(max_length=20, primary_key=True)
    ClaimDate = models.DateTimeField()
    HospitalStartDate = models.DateTimeField()
    HospitalEndDate = models.DateTimeField()
    PatientCoPay = models.IntegerField(default=0)
    ProviderID = models.ForeignKey(Provider, db_column='ProviderID', on_delete=models.CASCADE)
    ReasonID = models.ForeignKey(ReasonForDenial, db_column='ReasonID', on_delete=models.CASCADE)
    StaffID = models.ForeignKey(Staff, db_column='StaffID', on_delete=models.CASCADE)
    ClaimStatus = models.CharField(max_length=20)
    OpenDate = models.DateTimeField()
    ApproveDate = models.DateTimeField()
    DenyDate = models.DateTimeField()
    RejectDate = models.DateTimeField()
    RepealDate = models.DateTimeField()
    Notes = models.CharField(max_length=20)

    def __str__(self):
        return self.ClaimID

#    def get_absolute_url(self):
#        return reverse ('index')
    class Meta:
        managed = False
        db_table = 'Claim'
        app_label = 'website'


class Condition(models.Model):
    ConditionId = models.CharField(max_length=20, primary_key=True)
    ServiceId = models.ForeignKey(Service, on_delete=models.CASCADE)
    PolicyId = models.ForeignKey(Policy, on_delete=models.CASCADE)

class ServiceReceived(models.Model):
    ServiceId = models.CharField(max_length=20, primary_key=True)
    ServiceStartDate = models.DateTimeField()
    ServiceEndDate = models.DateTimeField()
    ServiceName = models.CharField(max_length=20)
    ServiceCost = models.IntegerField(default=0)
    PatientId = models.ForeignKey(Patient, on_delete=models.CASCADE)
    ProviderId = models.ForeignKey(Provider, on_delete=models.CASCADE)
    ClaimId = models.ForeignKey(Claim, on_delete=models.CASCADE)
    ServiceTypeId = models.ForeignKey(Service, on_delete=models.CASCADE)
    PolicyId = models.ForeignKey(Policy, on_delete=models.CASCADE)

