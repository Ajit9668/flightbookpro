from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import flightbookdata
import random

def bookingview(request):
    return render(request,'flightbookapp/book.html')

def inputview(request):
    if request.method=='GET':
        return render(request,'flightbookapp/input.html')
    else:
        flightbookdata(
            passenger=request.POST['passenger'],
            source=request.POST['source'],
            destination=request.POST['destination'],
            date=request.POST['date'],
            seat=random.randint(1,30)
        ).save()
        return HttpResponse('Seat Booked')

def resultview(request):
    data=flightbookdata.objects.all()
    return render(request,'flightbookapp/result.html',{'data':data})


