from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact

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
        contact.save()

    return render(request, "contact.html")
