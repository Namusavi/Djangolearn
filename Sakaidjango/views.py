from django.shortcuts import render


def aboutpage(request):
    return render(request, "about.html")


def servicespage(request):
    return render(request,"services.html")

def projectspage(request):
    return render(request,"projects.html")

def blogpage(request):
    return render(request,"blog.html")

def indexpage(request):
    return render(request,"index.html")

def signuppage(request):
    return render(request,"signup.html")