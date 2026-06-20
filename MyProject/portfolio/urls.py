from django.urls import path
from .views import home,about,contact,education,projects,skills,certificates

urlpatterns = [
    
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('skills/', skills, name='skills'),
    path('projects/', projects, name='projects'),
    path('education/', education, name='education'),
    path('certificates/', certificates, name='certificates'),
     path('contact/', contact, name='contact'),
]
