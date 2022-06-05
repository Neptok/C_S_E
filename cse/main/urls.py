

from main import views
from django.urls import path


urlpatterns = [
    path('',views.landingPage,name="landing page"),
    path('admission',views.admission,name="admission page"),
    path('contactus',views.contact,name="contact page"),
    path('plans',views.plans,name="plans page"),
    path('patners',views.patners,name="patners page")
]
