from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Client

def index(request):
    clients = Client.objects.all()

    context = {
        'clients':clients
    }
    return render(request, 'index.html', context)

def details(request, id):
    client = Client.objects.get(id=id)
    context = {
        'client':client
    }
    return render(request, 'details.html', context)


def add(request):
    if(request.method == 'POST'):
        name = request.POST['name']
        email = request.POST['email']

        client = Client(name=name, email=email)
        client.save()

        return redirect('/clients')
    else:
        return render(request, 'add.html')
