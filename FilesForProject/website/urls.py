from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('logout/',views.logout_user, name='logout'),
    path('transaction_record/<int:pk>',views.transaction_record, name='transaction_record'),
    path('delete_transaction/<int:pk>',views.delete_transaction, name='delete_transaction'),
    path('update_transaction/<int:pk>',views.update_transaction, name='update_transaction'),
    path('add_transaction/',views.add_transaction, name='add_transaction'),


    path('add_patient/',views.add_patient,name="add_patient"),
    path('patient_view/',views.patient_view, name="patient_view"),
    path('delete_patient/<int:pk>',views.delete_patient, name='delete_patient'),
    path('patient_record/<int:pk>',views.patient_record, name='patient_record'),
    path('update_patient/<int:pk>',views.update_patient, name='update_patient'),
]

