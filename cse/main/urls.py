

from main import views
from django.urls import path


urlpatterns = [
    path('',views.landingPage,name="landing page"),
    path('courses',views.courses,name="courses"),
    path('about',views.about,name="ABout page"),
    path('admission',views.admission,name="admission page"),
    path('contactus',views.contact,name="contact page"),
    path('plans',views.plans,name="plans page"),
    path('patners',views.patners,name="patners page"),
    path('mail',views.mailtest,name='mail page')

]
