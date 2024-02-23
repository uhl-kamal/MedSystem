from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Transaction, Patient
from .forms import TransactionForm, PatientForm
from django.http import HttpResponse

def home(request):
    t_records = Transaction.objects.all()


    #Check to see if logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate 
        user = authenticate(request, username=username, password=password)
        if user is not None: 
            login(request, user)
            messages.success(request, "Login successful")
            return redirect('home')
        else:
            messages.success(request, "Login unsuccessful")
            return redirect('home')
    else:    
        return render(request, "home.html", {"t_records":t_records})


def logout_user(request):
    logout(request)
    messages.success(request, "Logout successful")
    return redirect('home')


#New view for adding records 
def add_transaction(request):
	tform = TransactionForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if tform.is_valid():
				add_record = tform.save()
				messages.success(request, "Transaction Added")
				return redirect('home')
		return render(request, 'add_record.html', {'tform':tform})
	else:
		messages.success(request, "Login required")
		return redirect('home')
	

def add_patient(request):
	pform = PatientForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if pform.is_valid():
				add_patient = pform.save()
				messages.success(request, "Patient Added")
				return redirect('patient_view')
		return render(request, 'add_patient.html', {'pform':pform})
	else:
		messages.success(request, "Login required")
		return redirect('home')	
	
#View to get objects from patient table
def patient_view(request):
    p_records = Patient.objects.all()
    return render(request, "patient_view.html", {"p_records":p_records})


#View to see transaction record
def transaction_record(request, pk):
    if request.user.is_authenticated:
        transaction_record = Transaction.objects.get(id=pk)
        return render(request, "transaction_record.html",{"transaction_record":transaction_record})
    else: 
        messages.success("Login required")
        return redirect('home')
    

#View to delete transaction
def delete_transaction(request, pk):
        if request.user.is_authenticated:
            delete_transaction = Transaction.objects.get(id=pk)
            delete_transaction.delete()
            messages.success(request, "Transaction deleted")
            return redirect('home')
        else:
            messages.success(request, "Login required")
            return redirect('home')
	
#View to update transaction
def update_transaction(request, pk):
	if request.user.is_authenticated:
		current_record = Transaction.objects.get(id=pk)
		form = TransactionForm(request.POST or None, instance=current_record)
		if form.is_valid():
			form.save()
			messages.success(request, "Record updated")
			return redirect('home')
		return render(request, 'update_record.html', {'form':form})
	else:
		messages.success(request, "Login required")
		return redirect('home')



#View to see patient record
def patient_record(request, pk):
    if request.user.is_authenticated:
        patient_record = Patient.objects.get(id=pk)
        return render(request, "patient_record.html",{"patient_record":patient_record})
    else: 
        messages.success("Login required")
        return redirect('home')

#View to delete patient record
def delete_patient(request, pk):
        if request.user.is_authenticated:
            delete_patient = Patient.objects.get(id=pk)
            delete_patient.delete()
            messages.success(request, "Patient deleted")
            return redirect('patient_view')
        else:
            messages.success(request, "Login required")
            return redirect('home')

#View to update patient
def update_patient(request, pk):
	if request.user.is_authenticated:
		patient_record = Patient.objects.get(id=pk)
		pform = PatientForm(request.POST or None, instance=patient_record)
		if pform.is_valid():
			pform.save()
			messages.success(request, "Record updated")
			return redirect('patient_view')
		return render(request, 'update_patient.html', {'pform':pform})
	else:
		messages.success(request, "Login required")
		return redirect('home')
