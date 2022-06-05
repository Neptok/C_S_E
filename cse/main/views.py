from django.http import HttpResponse
from django.shortcuts import render

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