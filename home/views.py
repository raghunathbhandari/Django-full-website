from datetime import datetime
from multiprocessing import context
from django.shortcuts import render, HttpResponse, redirect
from home.models import Contact, Register, Users
from django.contrib import messages


# Create your views here Home Page.
def index(request):
    context = {
        'variable': "This is server value",
        'variable2': "Python is Great"
    }
    return render(request, 'index.html', context)
    # return HttpResponse ("This is Home page")

def about(request):
    return render(request, 'about.html')
    # return HttpResponse ("This is About Page ")

def servieces(request):
    return render(request, 'services.html')
    # return HttpResponse ("This is Services Page")

def userdetails(request):
    user_data = Register.objects.all()
    context = { 'usersdetails': user_data}
    return render(request, 'users.html',context)
    # return HttpResponse ("This is Services Page")

def register(request):
    if request.method == "POST":
        name = request.POST.get('name')
        emailid = request.POST.get('emailid')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        ocupation = request.POST.get('ocupation')
        details = request.POST.get('details')
        date = datetime.today()
        register = Register(name=name, emailid=emailid, phone=phone, ocupation=ocupation, details=details, address=address, date=date)
        register.save()
        messages.success(request, 'You are registered successfully !')

    return render(request, 'register.html')
    # return HttpResponse ("This is Services Page")


def deletuser(request):
    if request.method == "POST":
        id = request.POST.get('id')
        user = Register.objects.get(id=id)
        user.delete()
        return redirect('/userdetails')
        # messages.success(request, 'User has been Deleted successfully !')
        # print(id)


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        emailid = request.POST.get('emailid')
        phone = request.POST.get('phone')
        details = request.POST.get('details')
        contact = Contact(name=name, emailid=emailid, phone=phone, details=details, date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent successfully !')

    return render(request, 'contact.html')
    # return HttpResponse ("This is Services Page")



