import pyautogui
from django.shortcuts import render, redirect
from django.contrib import auth
from viewer.models import priceMovies, customerBooking
from .models import mainSlide, newRelease


# Create your views here.
def login(request):
    return render(request, 'employee/login.html')


def logging(request):
    if request.method == 'POST':
        username = request.POST['username']
        request.session["user"] = username
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            pyautogui.alert("Successfully logged in")
            return redirect(empDashboard)
        else:
            pyautogui.alert("Wrong Username or Password")
            return redirect('/')
    else:
        return redirect('/')


def logout(request):
    auth.logout(request)
    return redirect('/employee/')


def empDashboard(request):
    labels = []
    data = []
    querySet = priceMovies.objects.order_by('-price')[:5]
    for i in querySet:
        labels.append(i.name)
        data.append(i.price)
    q = priceMovies.objects.all()
    sum = 0
    for i in q:
        sum += i.price
    m = max(data)
    i = data.index(m)
    l, d = labels[i], data[i]
    main = mainSlide.objects.all().count()
    new = newRelease.objects.all().count()
    return render(request, 'employee/dashboard.html', {'labels': labels, 'data': data, 'sum': sum, 'l': l, 'd': d, 'main': main, 'new': new})


def mainSlideTable(request):
    m = mainSlide.objects.all()
    return render(request, 'employee/mainSlideTable.html', {'mainSlide': m})


def mainSlideAdd(request):
    return render(request, 'employee/mainSlideAdd.html')


def mainSlideAdded(request):
    if request.method == 'POST':
        movieName = request.POST.get('movieName')
        description = request.POST.get('description')
        trailer = request.POST.get('trailer')
        if request.FILES['pict']:
            image = request.FILES['pict']
            o = mainSlide(movieName=movieName, description=description, trailer=trailer, image=image)
            o.save()
            pyautogui.alert("Upload Done")
            return redirect('/employee/mainSlideTable')


def newReleaseTable(request):
    n = newRelease.objects.all()
    return render(request, 'employee/newReleaseTable.html', {'newRelease': n})


def newReleaseAdd(request):
    return render(request, 'employee/newReleaseAdd.html')


def newReleaseAdded(request):
    if request.method == 'POST':
        movieName = request.POST.get('movieName')
        description = request.POST.get('description')
        trailer = request.POST.get('trailer')
        price = request.POST.get('price')
        hour = request.POST.get('hour')
        rating = request.POST.get('rating')
        minute = request.POST.get('minute')
        if request.FILES['pict']:
            image = request.FILES['pict']
            o = newRelease(movieName=movieName, description=description, trailer=trailer, image=image, price=price, hour=hour, minute=minute, rating=rating)
            o.save()
            o = newRelease.objects.get(trailer=trailer)
            pyautogui.alert("Upload Done")
            return redirect('/employee/newReleaseTable')


def newReleaseDelete(request, id):
    m = newRelease.objects.get(pk=id).delete()
    return redirect('/employee/newReleaseTable')


def customerPaymentTable(request):
    p = customerBooking.objects.all()
    return render(request, 'employee/customerPayment.html', {'c': p})


def newReleaseEdit(request, id):
    m = newRelease.objects.get(pk=id)
    return render(request, 'employee/newReleaseEdit.html', {'m': m})


def newReleaseEdited(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        movieName = request.POST.get('movieName')
        description = request.POST.get('description')
        trailer = request.POST.get('trailer')
        price = request.POST.get('price')
        hour = request.POST.get('hour')
        rating = request.POST.get('rating')
        minute = request.POST.get('minute')
        o = newRelease.objects.get(id=id)
        o.movieName = movieName
        o.description = description
        o.trailer = trailer
        o.price = price
        o.hour = hour
        o.rating = rating
        o.minute = minute
        o.save()
        return redirect('/employee/newReleaseTable')


def mainSlideDelete(request, id):
    m = mainSlide.objects.get(pk=id).delete()
    return redirect('/employee/mainSlideTable')


def mainSlideEdit(request, id):
    m = mainSlide.objects.get(pk=id)
    return render(request, 'employee/mainSlideEdit.html', {'m': m})


def mainSlideEdited(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        movieName = request.POST.get('movieName')
        description = request.POST.get('description')
        trailer = request.POST.get('trailer')
        o = mainSlide.objects.get(id=id)
        o.movieName = movieName
        o.description = description
        o.trailer = trailer
        o.save()
        return redirect('/employee/mainSlideTable')
