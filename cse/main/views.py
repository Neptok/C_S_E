from django.http import HttpResponse
from django.shortcuts import render
from main import mailjet


CSEMailadd = "csebrt08@gmail.com"  #reciever mail

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
    if request.method == 'POST':
        formKey = ('fname','lname','course','dob','fatherName','motherName','number','gender','nationality','adress','description')

        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        course = request.POST.get('course')
        dob = request.POST.get('dob')
        fatherName = request.POST.get('fatherName')
        motherName = request.POST.get('motherName')
        number = request.POST.get('number')
        gender = request.POST.get('gender')
        nationality = request.POST.get('nationality')
        address = request.POST.get('address')
        description = request.POST.get('description')
        formData = [fname,lname,course,dob,fatherName,motherName,number,gender,nationality,address,description]
        messageBody = f''''
                    _-----------Someone applied for admission------------
                    Name = {fname + lname},
                    Course = {course},
                    Number = {number},
                    Address = {address}
                    $$$Further data$$$
                    FatherName = {fatherName}
                    Mothername = {motherName}
                    dob = {dob}
                    gender = {gender}
                    nationality = {nationality}
                    description = {description}
        '''
        mailResponse = mailjet.sendMail(CSEMailadd,'Admission Application',f'Someone applied for admission"',messageBody)
        return HttpResponse(mailResponse)
    else:
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
