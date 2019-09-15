from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    #return HttpResponse("Hello World!")
    return render(request, 'home.html', {'name': 'Inderpreet'})

def add(request):
    val1 = request.POST['num1']
    val2 = request.POST['num2']
    result = int(val1) + int(val2)
    return render(request, 'add_results.html', {'result': result})
