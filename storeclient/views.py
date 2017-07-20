from django.shortcuts import render
from clients.models import Client

def home(request):
        return render(request, 'home.html')

def list(request):
    clients = Client.objects.all()

    context = {
        'clients':clients
    }
    return render(request, 'list.html', context)


def add(request):
    if(request.method == 'POST'):
        name = request.POST['name']
        email = request.POST['email']

        client = Client(name=name, email=email)
        client.save()

        return redirect('/list')
    else:
        return render(request, 'add.html')

def details(request, id):
    client = Client.objects.get(id=id)
    context = {
        'client':client
    }
    return render(request, 'details.html', context)
