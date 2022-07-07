from django.http import HttpResponse
from django.shortcuts import render
from main import mailjet


CSEMailadd = "anjalishahjhau12345@gmail.com"

# Create your views here.
def landingPage(request):
    var = {
        'home':'active'
    }
    return render(request,'index.html',var)
def courses(request):
    var = {
        'courses':'active'
    }
    return render(request,'courses.html',var)
def about(request):
    var = {
        'about':'active'
    }
    return render(request,'about.html',var)
def admissionForm(request):
    var = {
        'admission':'active'
    }
    return render(request,'form.html',var)
def contact(request):
    var = {
        'contact':'active'
        
    }
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
         
        messageBody = f'''

            Some one trying  Contact u 
            Name : {fname} {lname}
            Email : {email}
            subject : {subject}
            Message : {message}
        '''
        print(messageBody)
        cursor = mailjet.sendMail(CSEMailadd,'CSE Contact form','Someone trying to contact ',  messageBody)

        return HttpResponse(f"{cursor}")
    else:
        return render(request,'contact.html',var)


def plans(request):
    var = {
        'plans':'active'
    }
    return HttpResponse("planspage")
def patners(request):
    var = {
        'patners':'active'
    }
    return HttpResponse("patnerspage")
  

def mailtest(self):
    cursor = mailjet.sendMail(CSEMailadd,'Got a mail','mera naam joker','Hello bro these is mailjet')

    return HttpResponse(f"{cursor}")
