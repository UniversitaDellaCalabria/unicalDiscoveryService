from django.urls import path, include

from . views import unical_spid_ds

app_name="unical_discovery_service"

urlpatterns = [
    path('', unical_spid_ds, name='unical_spid_ds'),
    path('unical/spid/ds', unical_spid_ds, name='unical_spid_ds'),
    path('role/idp.ds', unical_spid_ds, name='unical_spid_ds'),
]
