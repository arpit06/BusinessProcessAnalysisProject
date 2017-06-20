from django.db import models

# Create your models here.
from django.db import models
from django.core.urlresolvers import reverse
from datetime import date

class Patient(models.Model):
    gender_choices = (
        ('Male', 'Male'), ('Female', 'Female'),
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
    patientid = models.CharField("Patient ID", db_column='PatientID', primary_key=True, max_length=20)  # Field name made lowercase.
    firstname = models.CharField("First Name", db_column='FirstName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField("Last Name", db_column='LastName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField("Gender", db_column='Gender', choices=gender_choices, max_length=255, blank=True, null=True)  # Field name made lowercase.
    patientaddress = models.CharField("Address Line1", db_column='PatientAddress', max_length=255, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField("City", db_column='City', max_length=255, blank=True, null=True)  # Field name made lowercase.
    patientstate = models.CharField("State", db_column='PatientState', choices=State_choice, max_length=255, blank=True, null=True)  # Field name made lowercase.
    zipcode = models.IntegerField("Zip Code", db_column='ZipCode', blank=True, null=True)  # Field name made lowercase.
    phonenumber = models.CharField("Phone Number", db_column='PhoneNumber', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dateofbirth = models.DateField("Date of Birth", db_column='DateOfBirth', blank=True, null=True)  # Field name made lowercase.
    employment = models.NullBooleanField("Employment",db_column='Employment', blank=True, null=True)  # Field name made lowercase.
    age = models.IntegerField("Age", db_column='Age', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.firstname + " " + self.lastname

    class Meta:
        managed = False
        db_table = 'Patient'


class Pharmacy(models.Model):
    pharmacyid = models.CharField(db_column='pharmacyId', max_length=20)  # Field name made lowercase.
    pharmacistid = models.CharField(db_column='pharmacistId', max_length=20)  # Field name made lowercase.
    technicianid = models.CharField(db_column='technicianId', max_length=20)  # Field name made lowercase.
    pharmacyname = models.CharField(db_column='pharmacyName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    pharmacylocation = models.CharField(db_column='pharmacyLocation', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Pharmacy'
        unique_together = (('pharmacyid', 'pharmacistid', 'technicianid'),)


class Physician(models.Model):
    physicianid = models.CharField(db_column='physicianId', primary_key=True, max_length=20)  # Field name made lowercase.
    physicianfirstname = models.CharField(db_column='physicianFirstName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    physicianlastname = models.CharField(db_column='physicianLastName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    physicianphonenumber = models.CharField(db_column='physicianPhoneNumber', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Physician'


class Policy(models.Model):
    policyid = models.CharField(db_column='PolicyID', primary_key=True, max_length=20)  # Field name made lowercase.
    policyname = models.CharField(db_column='PolicyName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    duration = models.IntegerField(db_column='Duration', blank=True, null=True)  # Field name made lowercase.
    policytype = models.CharField(db_column='PolicyType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    patientid = models.CharField(db_column='PatientID', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Policy'

    def __str__(self):
        return self.policyname

class Provider(models.Model):
    type_choices = (
        ('PrimaryCare', 'PrimaryCare'), ('EmergencyCare', 'EmergencyCare'),
        ('Hospital', 'Hospital'), ('Pharmacy', 'Pharmacy'), ('Others', 'Others'),
    )
    network_choices = (
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

    providerid = models.CharField(db_column='ProviderID', primary_key=True, max_length=20)  # Field name made lowercase.
    providername = models.CharField(db_column='ProviderName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    providertype = models.CharField(db_column='ProviderType', choices=type_choices, max_length=255, blank=True, null=True)  # Field name made lowercase.
    networktype = models.CharField(db_column='NetworkType', choices=network_choices, max_length=255, blank=True, null=True)  # Field name made lowercase.
    provideraddress = models.CharField(db_column='ProviderAddress', max_length=255, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=255, blank=True, null=True)  # Field name made lowercase.
    providerstate = models.CharField(db_column='ProviderState', choices=State_choice, max_length=255, blank=True, null=True)  # Field name made lowercase.
    zipcode = models.IntegerField(db_column='ZipCode', blank=True, null=True)  # Field name made lowercase.
    phonenumber = models.CharField(db_column='PhoneNumber', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Provider'

    def __str__(self):
        return self.providername


class ReasonForDenial(models.Model):
    reasonid = models.CharField(db_column='ReasonID', primary_key=True, max_length=20)  # Field name made lowercase.
    reasondescription = models.CharField(db_column='ReasonDescription', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ReasonForDenial'

    def __str__(self):
        return self.reasondescription

class Services(models.Model):
    servicetypeid = models.CharField(db_column='ServiceTypeID', primary_key=True, max_length=20)  # Field name made lowercase.
    typename = models.CharField(db_column='TypeName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    servicecategory = models.CharField(db_column='ServiceCategory', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Services'

    def __str__(self):
        return self.typename + " " + self.servicecategory


class Staff(models.Model):
    STATUS_CHOICES = (
        ('Manager', 'Manager'), ('Reviewer', 'Reviewer'),
        ('Processor', 'Processor'),
    )
    staffid = models.CharField("Staff ID",db_column='StaffID', primary_key=True, max_length=20)  # Field name made lowercase.
    firstname = models.CharField("First Name",db_column='FirstName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField("Last Name", db_column='LastName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    staffrole = models.CharField("Role", db_column='StaffRole', choices=STATUS_CHOICES, max_length=255, default="")  # Field name made lowercase.
    susername = models.CharField("Select Username:",db_column='SUsername', max_length=50, blank=False, null=True)  # Field name made lowercase.
    spassword = models.CharField("Select Password",db_column='SPassword', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Staff'

    def __str__(self):
        return self.firstname + " " + self.lastname


class Conditions(models.Model):
    conditionid = models.CharField(db_column='ConditionID', primary_key=True, max_length=20)  # Field name made lowercase.
    servicetypeid = models.ForeignKey('Services', models.DO_NOTHING, db_column='ServiceTypeID')  # Field name made lowercase.
    policyid = models.ForeignKey('Policy', models.DO_NOTHING, db_column='PolicyID')  # Field name made lowercase.
    innetworkcoverage = models.CharField(db_column='InNetworkCoverage', max_length=255, blank=True, null=True)  # Field name made lowercase.
    outnetworkcoverage = models.CharField(db_column='OutNetworkCoverage', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Conditions'

class Druginventory(models.Model):
    drugid = models.CharField(db_column='drugId', primary_key=True, max_length=20)  # Field name made lowercase.
    drugkind = models.CharField(db_column='drugKind', max_length=20, blank=True, null=True)  # Field name made lowercase.
    drugname = models.CharField(db_column='drugName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    drugquantity = models.CharField(db_column='drugQuantity', max_length=20, blank=True, null=True)  # Field name made lowercase.
    inventorylocation = models.CharField(db_column='inventoryLocation', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DrugInventory'

class Druginventoryprescription(models.Model):
    drugid = models.ForeignKey(Druginventory, models.DO_NOTHING, db_column='drugId')  # Field name made lowercase.
    prescriptionid = models.CharField(db_column='prescriptionId', max_length=20)  # Field name made lowercase.
    fulfilled = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'DrugInventoryPrescription'
        unique_together = (('drugid', 'prescriptionid'),)

class Fulfilment(models.Model):
    fulfilmentid = models.CharField(db_column='fulfilmentId', primary_key=True, max_length=20)  # Field name made lowercase.
    datefilled = models.CharField(db_column='dateFilled', max_length=20, blank=True, null=True)  # Field name made lowercase.
    receiverfirstname = models.CharField(db_column='receiverFirstName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    receiverlastname = models.CharField(db_column='receiverLastName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    generic = models.CharField(max_length=20, blank=True, null=True)
    pharmacistid = models.ForeignKey('Pharmacy', models.DO_NOTHING, db_column='pharmacistId', blank=True, null=True,related_name='Pharmacist1')  # Field name made lowercase.
    technicianid = models.ForeignKey('Pharmacy', models.DO_NOTHING, db_column='technicianId', blank=True, null=True, related_name='Technician1')  # Field name made lowercase.
    pharmacyid = models.ForeignKey('Pharmacy', models.DO_NOTHING, db_column='pharmacyId', blank=True, null=True, related_name='Pharmacy1')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Fulfilment'



class Prescription(models.Model):
    patientid = models.ForeignKey(Patient, models.DO_NOTHING, db_column='PatientID')  # Field name made lowercase.
    physicianid = models.ForeignKey(Physician, models.DO_NOTHING, db_column='physicianId')  # Field name made lowercase.
    fulfilmentid = models.ForeignKey(Fulfilment, models.DO_NOTHING, db_column='fulfilmentId')  # Field name made lowercase.
    prescriptionid = models.CharField(db_column='prescriptionId', max_length=20)  # Field name made lowercase.
    dateissued = models.CharField(db_column='dateIssued', max_length=20, blank=True, null=True)  # Field name made lowercase.
    numberissued = models.CharField(db_column='numberIssued', max_length=20, blank=True, null=True)  # Field name made lowercase.
    dosagenumber = models.CharField(db_column='dosageNumber', max_length=20, blank=True, null=True)  # Field name made lowercase.
    dosagefrequency = models.CharField(db_column='dosageFrequency', max_length=20, blank=True, null=True)  # Field name made lowercase.
    purpose = models.CharField(max_length=20, blank=True, null=True)
    drugid = models.ForeignKey(Druginventory, models.DO_NOTHING, db_column='drugId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Prescription'
        unique_together = (('patientid', 'physicianid', 'fulfilmentid', 'prescriptionid'),)


class Claim(models.Model):
    claimstatus_choices = (
        ('Open', 'Open'), ('In Progress', 'In Progress'),
        ('Deny', 'Deny'),('Repeal', 'Repeal'),('Reject', 'Reject'),('Approve', 'Approve'),
    )
    claimid = models.CharField("Claim ID", db_column='ClaimID', primary_key=True, max_length=20)  # Field name made lowercase.
    claimdate = models.DateField("Claim Date",db_column='ClaimDate', blank=True, null=True)  # Field name made lowercase.
    hospitalstartdate = models.DateField("Start Date of Hospital State", db_column='HospitalStartDate', blank=True, null=True)  # Field name made lowercase.
    hospitalenddate = models.DateField("End Date of Hospital State", db_column='HospitalEndDate', blank=True, null=True)  # Field name made lowercase.
    patientcopay = models.IntegerField("Co-Pay Value", db_column='PatientCoPay', blank=True, null=True)  # Field name made lowercase.
    providerid = models.ForeignKey(Provider, models.DO_NOTHING, db_column='ProviderID', blank=True, null=True)  # Field name made lowercase.
    reasonid = models.ForeignKey(ReasonForDenial, models.DO_NOTHING, db_column='ReasonID', blank=True, null=True)  # Field name made lowercase.
    staffid = models.ForeignKey(Staff, models.DO_NOTHING, db_column='StaffID', blank=True, null=True)  # Field name made lowercase.
    claimstatus = models.CharField("Status",db_column='ClaimStatus', max_length=20, blank=True, null=True, default="Open",choices=claimstatus_choices)  # Field name made lowercase.
    opendate = models.DateField("Open Date", db_column='OpenDate', blank=True, null=True, default=date.today())  # Field name made lowercase.
    approvedate = models.DateField("Approve Date", db_column='ApproveDate', blank=True, null=True)  # Field name made lowercase.
    denydate = models.DateField("Deny Date", db_column='DenyDate', blank=True, null=True)  # Field name made lowercase.
    rejectdate = models.DateField("Reject Date", db_column='RejectDate', blank=True, null=True)  # Field name made lowercase.
    repealdate = models.DateField("Repeal Date", db_column='RepealDate', blank=True, null=True)  # Field name made lowercase.
    notes = models.CharField("Notes", db_column='Notes', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Claim'

    def __str__(self):
        return self.claimid

class ServiceReceived(models.Model):
    serviceid = models.CharField("ID",db_column='ServiceID', primary_key=True, max_length=20)  # Field name made lowercase.
    servicename = models.CharField("Name",db_column='ServiceName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    startdate = models.DateField("Start Date",db_column='StartDate', blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateField("End Date",db_column='EndDate', blank=True, null=True)  # Field name made lowercase.
    cost = models.IntegerField("Cost",db_column='Cost', blank=True, null=True)  # Field name made lowercase.
    patientid = models.ForeignKey(Patient, models.DO_NOTHING, db_column='PatientID', blank=True, null=True)  # Field name made lowercase.
    providerid = models.ForeignKey(Provider, models.DO_NOTHING, db_column='ProviderID', blank=True, null=True)  # Field name made lowercase.
    claimid = models.ForeignKey(Claim, models.DO_NOTHING, db_column='ClaimID', blank=True, null=True)  # Field name made lowercase.
    servicetypeid = models.ForeignKey(Services, models.DO_NOTHING, db_column='ServiceTypeID', blank=True, null=True)  # Field name made lowercase.
    policyid = models.ForeignKey(Policy, models.DO_NOTHING, db_column='PolicyID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ServiceReceived'

    def __str__(self):
        return self.servicename
