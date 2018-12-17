from django.shortcuts import render, HttpResponse
from .models import Useless, Unless

def index(request):
    test = Unless.objects.get(id=1)
    x = test.z.two
    #print(testone)
    print(Unless.objects.all().values())
    return HttpResponse(x)

def battle(request):

    return render(request, "mon_app/battle.html")

# Create your views here.
