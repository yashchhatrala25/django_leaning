from django.http import HttpResponse
from django.shortcuts import render

def homePage(request):
    # data={
    #     'title': 'Home',
    #     'bdata': 'Welcome to Home Page | Dynamic Data',
    #     'clist': ['PHP', 'Java', 'Python'],
    #     'numbers': [],
    #     'student_details': [
    #         {'name': 'yash', 'phone': 123456789},
    #         {'name': 'john', 'phone': 896764464},
    #     ]
    # }
    return render(request, "index.html")

def aboutUs(request):
    return render(request, 'about.html')

def service(request):
    return render(request, 'service.html')

def faeature(request):
    return render(request, 'feature.html')

def ourDoctors(request):
    return render(request, 'team.html')

def appointment(request):
    return render(request, 'appointment.html')

def testimonial(request):
    return render(request, 'testimonial.html')

def pageNotFound(request):
    return render(request, '404.html')

def contactUs(request):
    return render(request, 'contact.html')