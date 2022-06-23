from django.http import HttpResponse
from django.shortcuts import render
from main import mailjet


# Create your views here.
def landingPage(request):
    return render(request,'index.html')
def courses(request):
    return render(request,'courses.html')
def about(request):
    return render(request,'about.html')
def admission(request):
    return HttpResponse("admissionpage")
def contact(request):
    return render(request,'contact.html')
def plans(request):
    return HttpResponse("planspage")
def patners(request):
    return HttpResponse("patnerspage")


def mailtest(self):
    mailjet.sendMail()
    return HttpResponse("Mail sent check your mail")