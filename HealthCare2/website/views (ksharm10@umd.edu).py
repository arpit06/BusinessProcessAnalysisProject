from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView,FormView
from django.views.generic import TemplateView,ListView
from .models import Staff, Patient, Provider, Claim, ReasonForDenial,ServiceReceived
from django.core.urlresolvers import reverse_lazy
from django.forms import ModelForm,DateField
from django.forms.extras.widgets import SelectDateWidget


# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request, 'website/index.html')

def staffindex(request):
    return render(request, 'website/staff_index.html')

def login1(request):
    if "login1-button" in request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user1 = Staff.objects.get(susername=username)
        if user1.spassword == password:
            if user1.staffrole == 'Manager':
                return redirect('index')
            else:
                return redirect('view-claim')
        else:
            return render(request, 'website/login1.html')
    else:
        return render(request, 'website/login1.html')



class StaffCreate(CreateView):
    model = Staff
    fields = ['staffid', 'firstname', 'lastname', 'staffrole', 'susername', 'spassword']
    success_url = reverse_lazy('index')

class StaffRead(ListView):
    model = Staff

class StaffUpdate(UpdateView):
    model = Staff
    success_url = reverse_lazy('view-staff')
    fields = ['staffid', 'firstname', 'lastname', 'staffrole', 'susername', 'spassword']


class StaffDelete(DeleteView):
    model = Staff
    success_url = reverse_lazy('view-staff')

##########################################################
#class PatientCreate(CreateView):
#    model = Patient
#    fields = ['patientid', 'firstName', 'lastName', 'gender','patientaddress', 'city', 'patientstate', 'zipcode',
#              'phoneNumber','dateofbirth','employment','age']
#    success_url = reverse_lazy('index')

class PatCreatForm(ModelForm):
  class Meta:
    model = Patient
    #DateOfBirth = DateField(widget=SelectDateWidget())
    widgets = {
      'dateofbirth': SelectDateWidget(years=range(1950, 2017)),
    }
    fields = '__all__'
    exclude = ['age']


#class PatAdmin(ModelAdmin):
#  form = PatCreatForm

class PatientCreate(FormView):
    template_name='website/patient_form.html'
    form_class=PatCreatForm
    success_url = reverse_lazy('index')

    def form_valid(self,form):
        form.save()
        return redirect('index')

class PatientUpdate(UpdateView):
    model = Patient
    success_url = reverse_lazy('view-patient')
    fields = ['patientid', 'firstname', 'lastname', 'gender', 'patientaddress', 'city', 'patientstate', 'zipcode',
              'phonenumber', 'dateofbirth', 'employment']

class PatientDelete(DeleteView):
    model = Patient
    success_url = reverse_lazy('view-patient')

class PatientRead(ListView):
    model = Patient

##########################################################

class ProviderCreate(CreateView):
    model = Provider
    fields = ['providerid','providername','providertype','networktype','provideraddress','city','providerstate',
              'zipcode','phonenumber']
    success_url = reverse_lazy('index')

class ProviderRead(ListView):
    model = Provider

class ProviderUpdate(UpdateView):
    model = Provider
    success_url = reverse_lazy('view-provider')
    fields = ['providerid', 'providername', 'providertype', 'networktype', 'provideraddress', 'city', 'providerstate',
              'zipcode', 'phonenumber']


class ProviderDelete(DeleteView):
    model = Provider
    success_url = reverse_lazy('view-provider')

###################################################

#class ClaimCreate(CreateView):
#    model = Claim
#    fields = ['claimid', 'claimdate', 'hospitalstartdate','hospitalenddate', 'patientcopay', 'providerid']
#    success_url = reverse_lazy('create-service')

class claimCreatForm(ModelForm):
  class Meta:
    model = Claim
    widgets = {
        'claimdate': SelectDateWidget(years=range(2015, 2017)),
        'hospitalstartdate': SelectDateWidget(years=range(2015, 2017)),
        'hospitalenddate': SelectDateWidget(years=range(2015, 2017)),
    }
    fields = '__all__'
    exclude = ['reasonid','staffid', 'claimstatus', 'opendate', 'approvedate', 'denydate',
              'rejectdate', 'repealdate', 'notes']

class ClaimCreate(FormView):
    template_name='website/claim_form.html'
    form_class=claimCreatForm
    success_url = reverse_lazy('create-service')

    def form_valid(self,form):
        form.save()
        return redirect('create-service')

class ClaimRead(ListView):
    model = Claim

class ClaimReadMgr(ListView):
    model = Claim
    template_name = 'website/claim_list_mgr.html'

class ClaimUpdate(UpdateView):
    model = Claim
    fields = ['claimid', 'providerid', 'reasonid','staffid', 'claimstatus', 'opendate', 'approvedate', 'denydate',
              'rejectdate', 'repealdate', 'notes']
    success_url = reverse_lazy('view-claim')

class ClaimUpdateByManager(UpdateView):
    model = Claim
    fields = ['claimid', 'providerid', 'reasonid','staffid', 'claimstatus', 'opendate']
    success_url = reverse_lazy('view-claim-mgr')

class ClaimDelete(DeleteView):
    model = Claim
    success_url = reverse_lazy('view-claim')

###################################
#Services

class ServiceCreate(CreateView):
    model=ServiceReceived
    success_url=reverse_lazy('create-service')
    fields = ['serviceid','servicename','startdate','enddate','cost','patientid','providerid','claimid','servicetypeid',
              'policyid']

class ServiceRead(ListView):
    model=ServiceReceived