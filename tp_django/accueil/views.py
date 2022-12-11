from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
import datetime


def helloWorld(request):
    date=datetime.datetime.now()
    return render(request,'accueil/helloWorld.html',{'date':date})


def sum(request, val1, val2):
    somme= int(val1) + int(val2)
    return render(request,'accueil/sum.html',{'somme':somme} )