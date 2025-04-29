from django.http import HttpResponse
from django.shortcuts import render

def homePage(request):
    data={
        'title': 'Home',
        'bdata': 'Welcome to Home Page | Dynamic Data',
        'clist': ['PHP', 'Java', 'Python'],
        'numbers': [],
        'student_details': [
            {'name': 'yash', 'phone': 123456789},
            {'name': 'john', 'phone': 896764464},
        ]
    }
    return render(request, "index.html", data)

def aboutUs(request):
    return HttpResponse("<h1>Welcome to About Page</h1>")

def course(request):
    return HttpResponse("<h1>Welcome to Course Page</h1>")

def courseDetails(request, courseid):
    return HttpResponse(courseid)