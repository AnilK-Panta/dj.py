from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, "index.html")
    # return HttpResponse("This is home page")

def about(request):
    return render(request, "about.html")

def services(request):
    return render(request, "service.html")

def blog(request):
    return render(request, "blog.html")

def contact(request):
    if request.method == "POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        phone=request.POST.get("phone")
        message=request.POST.get("message")
        contact=Contact(name=name, email=email, phome=phone, message=message, date=datetime.today())
        
        if(name or email or phone or message):
            messages.success(request, 'Thankyou your message was sent')
            contact.save()
        else:
            messages.warning(request, "Your field is empty")

    return render(request, "contact.html")
