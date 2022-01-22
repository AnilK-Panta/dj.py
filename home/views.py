from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context={
"variable": "I have passed a props in django",
"value": 101,
"lolipop": "django is beautiful"
    }
    return render(request, "index.html", context)
    # return HttpResponse("This is home page")

def about(request):
    return HttpResponse("This is about page")

def contact(request):
    return HttpResponse("This is contact page")

def blog(request):
    return HttpResponse("This is blog page")
