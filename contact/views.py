from django.shortcuts import render,redirect
from .models import ContactMOdels
from django.urls import reverse

# Create your views here.

def index(request):
    contacts = ContactMOdels.objects.all()
    search_input = request.GET.get('search-area')
    if search_input:
        contacts  = ContactMOdels.objects.filter(full_name__icontains=search_input)
    else:
        contacts=ContactMOdels.objects.all()
        search_input=''
    return render (request,'index.html',{'users':contacts,'search':search_input})

def CreateContact(request):
    if request.method == "POST":
        new_contact = ContactMOdels(
            full_name = request.POST['fullname'],
            reletionship = request.POST['relationship'],
            phone_number = request.POST['phone-number'],
            email = request.POST['email'],
            address = request.POST['address'],


        )
        new_contact.save()
        return redirect('/')
    return render(request,'create.html')

def Profile(request,pk):
    contact = ContactMOdels.objects.get(id=pk)
    return render(request,'contact-profile.html',{'contact':contact})

def EditContact(request,pk):
    EditCon = ContactMOdels.objects.get(id=pk)

    if request.method == 'POST':
        EditCon.full_name = request.POST['fullname']
        EditCon.reletionship = request.POST['relationship']
        EditCon.email = request.POST['e-mail']
        EditCon.address =request.POST['address']
        EditCon.phone_number = request.POST['phone-number']

        EditCon.save()

        return redirect('/profile/' + str(EditCon.id))
    return render(request,'edit.html',{'edit':EditCon})

def DeleteContact(request,pk):
    deleteConc = ContactMOdels.objects.get(id=pk)
    if request.method == 'POST':
        deleteConc.delete()

        return redirect('index')
        
    
    return render(request,'delete.html',{'delete':deleteConc})

def sample():
    pass