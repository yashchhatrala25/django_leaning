from django.http import HttpResponse
from django.shortcuts import render

def homePage(request):
    return render(request, "index.html")

def aboutUs(request):
    return HttpResponse("<h1>Welcome to About Page</h1>")

def course(request):
    return HttpResponse("<h1>Welcome to Course Page</h1>")

def courseDetails(request, courseid):
    return HttpResponse(courseid)