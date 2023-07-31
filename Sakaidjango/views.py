from django.shortcuts import render, redirect
from .models import People


def insertData(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        country = request.POST.get('country')
        city = request.POST.get('city')
        age = request.POST.get('age')
        gender = request.POST.get('gender')

        query = People.objects.create(name=name, email=email, phone=phone, country=country, city=city, age=age, gender=gender)

        query.save()
        return redirect("/")
    return render(request, "index.html")


def aboutpage(request):
    return render(request, "about.html")


def servicespage(request):
    return render(request, "services.html")


def projectspage(request):
    return render(request, "projects.html")


def blogpage(request):
    return render(request, "blog.html")


def indexpage(request):
    data = People.objects.all()
    context = {"data": data}
    return render(request, "index.html", context)


def signuppage(request):
    return render(request, "signup.html")


def deleteData(request, id):
    d = People.objects.get(id=id)
    d.delete()
    return redirect("/")
    return render(request, "index.html")


def updateData(request, id):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        country = request.POST.get('country')
        city = request.POST.get('city')
        age = request.POST.get('age')
        gender = request.POST.get('gender')

        edit_data = People.objects.get(id=id)
        edit_data.name = name
        edit_data.email = email
        edit_data.phone = phone
        edit_data.country = country
        edit_data.city = city
        edit_data.age = age
        edit_data.gender = gender
        edit_data.save()
        return redirect("/")

    dta = People.objects.get(id=id)
    context = {"dta": dta}
    return render(request, "edit.html", context)
