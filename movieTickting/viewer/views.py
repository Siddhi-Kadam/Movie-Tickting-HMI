import pyautogui
from django.core.mail import EmailMultiAlternatives
from movieTickting.settings import EMAIL_HOST_USER
from django.shortcuts import render, redirect
from employee.models import mainSlide, newRelease

# Create your views here.
from viewer.models import customerBooking, priceMovies


def homePage(request):
    mainSlider = mainSlide.objects.all()
    newReleased = newRelease.objects.all()
    return render(request, 'viewer/homePage.html', {'mainSlider': mainSlider, 'newRelease': newReleased})


def book(request, id):
    m = newRelease.objects.get(id=id)
    return render(request, 'viewer/book.html', {'d': m})


def pay(request):
    if request.method == 'POST':
        names = request.POST.get('names')
        emails = request.POST.get('emails')
        nos = request.POST.get('nos')
        seats = request.POST.get('seats')
        cost = request.POST.get('cost')
        movies = request.POST.get('movies')
        print("Details: ", names, emails, nos, seats, cost, movies)
        m = customerBooking(name=names, email=emails, seats=seats, noOfSeats=nos, cost=cost, movie=movies)
        m.save()
        ids = request.POST.get('ids')
        mo = priceMovies.objects.get(ids=ids)
        c = mo.price
        mo.price = int(c) + int(cost)
        mo.save()
        subject = 'Moviezz - Tickets Successfully Booked'
        content = 'Moviezz - Tickets Successfully Booked'
        html = 'Dear ' + names + ',<br>Thanks for booking movie tickets for ' + movies + ' today at 5PM with us. Payment is done of Rs.' + cost + '. Booked seats are ' + seats + '. You could locate us through google maps using <a href="https://goo.gl/maps/FcC5BtmKNzoXGohB8">this</a>.<br>QR Code for billing details. <br><img height="60" width="60" src="https://worldbarcodes.com/wp-content/assets/sites/4/QR-Code-Standard1.jpg">.<br>Thank You.'
        msg = EmailMultiAlternatives(f'{subject}', f'{content}', EMAIL_HOST_USER, [f'{emails}'])
        msg.attach_alternative(html, "text/html")
        msg.send()
        return render(request, 'viewer/payment.html', {'names': names, 'emails': emails, 'nos': nos, 'seats': seats,
                                                       'cost': cost, 'movies': movies})


def contact(request):
    return render(request, 'viewer/contact.html')


def contacted(request):
    pyautogui.alert("Your message is successfully sent")
    return redirect('/contact')


def about(request):
    return render(request, 'viewer/about.html')
