from django.conf.urls import url

from . import views

urlpatterns = [
    #url(r'^$', views.index, name='index'),
    #url(r'^login1/$', views.login1, name='login1'),
    url(r'^$', views.login1, name='login1'),
    url(r'^manager/$', views.index, name='index'),
    url(r'^staff/$', views.staffindex, name='staff-index'),


    url(r'^patient/add/$', views.PatientCreate.as_view(), name='create-patient'),
    url(r'^patient/view/$', views.PatientRead.as_view(), name='view-patient'),
    url(r'^patient/delete/(?P<pk>\w+)$', views.PatientDelete.as_view(), name='delete-patient'),
    url(r'^patient/update/(?P<pk>\w+)$', views.PatientUpdate.as_view(), name='update-patient'),

    url(r'^provider/add/$', views.ProviderCreate.as_view(), name='create-provider'),
    url(r'^provider/view/$', views.ProviderRead.as_view(), name='view-provider'),
    url(r'^provider/delete/(?P<pk>\w+)$', views.ProviderDelete.as_view(), name='delete-provider'),
    url(r'^provider/update/(?P<pk>\w+)$', views.ProviderUpdate.as_view(), name='update-provider'),

    url(r'^staff/view/$', views.StaffRead.as_view(), name='view-staff'),
    url(r'^staff/delete/(?P<pk>\w+)$', views.StaffDelete.as_view(), name='delete-staff'),
    url(r'^staff/update/(?P<pk>\w+)$', views.StaffUpdate.as_view(), name='update-staff'),
    url(r'^staff/add/$', views.StaffCreate.as_view(), name='add-staff'),



    #claim processing
    url(r'^claims/view/$', views.ClaimRead.as_view(), name='view-claim'),
    url(r'^claims/delete/(?P<pk>\w+)$', views.ClaimDelete.as_view(), name='delete-claim'),
    url(r'^claims/update/(?P<pk>\w+)$', views.ClaimUpdate.as_view(), name='update-claim'),
    url(r'^provider/claim/add/$', views.ClaimCreate.as_view(), name='create-claim'),
]