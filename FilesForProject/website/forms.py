from django import forms
from . models import Patient, Transaction

#New model forms 
class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        exclude = ['id']
        widgets = {
            'Administration_DateTime': forms.DateTimeInput(
                format=('%d-%m-%Y T%H:%M'), attrs={'type': 'datetime-local'}
            )
        }          
        

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        exclude = ["id"]
        widgets = {
            'DOB': forms.DateInput(
                attrs={'type': 'date', 'class': 'form-control'}
            )
        }        

