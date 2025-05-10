"""
URL configuration for practice project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from practice import views

urlpatterns = [
    path('admin-panel/', admin.site.urls),
    path('', views.homePage, name='home'),
    path('about-us/', views.aboutUs, name='about-us'),
    path('service/', views.service, name='service'),    
    path('pages/faeature/', views.faeature, name='pages/faeature'),
    path('pages/team/', views.ourDoctors, name='pages/team'),
    path('pages/appointment/', views.appointment, name='pages/appointment'),
    path('pages/testimonial/', views.testimonial, name='pages/testimonial'),
    path('pages/404/', views.pageNotFound, name='pages/404'),
    path('contact/', views.contactUs, name='contact'),
]
