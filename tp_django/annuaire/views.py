from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse



contacts = [
   {
      "nom": "Cassidy",
      "prenom": "Hammond",
      "telephone": "03 94 96 50 97"
    },
    {
      "nom": "Charde",
      "prenom": "Hyde",
      "telephone": "03 44 84 02 60"
    },
    {
      "nom": "Dorian",
      "prenom": "Bailey",
      "telephone": "03 78 24 49 97"
    },
    {
      "nom": "Vivien",
      "prenom": "Duffy",
      "telephone": "03 26 81 80 44"
    },
    {
      "nom": "Ivory",
      "prenom": "Colon",
      "telephone": "03 85 87 65 55"
    }
]

def annuaire(request):
    return render(request,'annuaire/list.html', {'contacts':contacts})

def info(request, nom):
    for contact in contacts:
        if contact.nom == nom:
            return render(request,'annuaire/info.html', {'nom':contact.nom,'prenom':contact.prenom,'nom':contact.telephone})