from django.shortcuts import render
from travello.models import Destination

def index(request):
    #destination_1 = Destination()
    #destination_1.name = 'Mumbai'
    #destination_1.desc = 'City that never sleeps'
    #destination_1.price = 700
    #destination_1.img = 'destination_1.jpg'
    #destination_1.offer = False

    destinations = Destination.objects.all()

    #destinations = [destination_1, destination_2, destination_3]
    return render(request, 'index.html', {'destinations': destinations})
