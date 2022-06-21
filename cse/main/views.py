from django.http import HttpResponse
from django.shortcuts import render
from main import mailjet


# Create your views here.
def landingPage(request):
    return HttpResponse("Landingpage")
def admission(request):
    return HttpResponse("admissionpage")
def contact(request):
    return HttpResponse(" contactpage")
def plans(request):
    return HttpResponse("planspage")
def patners(request):
    return HttpResponse("patnerspage")


def mailtest(self):
    mailjet.sendMail()
    return HttpResponse("Mail sent check your mail")