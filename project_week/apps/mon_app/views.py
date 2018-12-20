from django.shortcuts import render, HttpResponse, redirect
from .models import Useless, Unless, Combat, MonsterOne

def index(request):
    test = Unless.objects.get(id=1)
    x = test.z.two
    #print(testone)
    print(Unless.objects.all().values())
    return HttpResponse(x)

def battle(request):

    return render(request, "mon_app/battle.html")

def create_monster(request):
    e = Combat.objects.all()
    v = MonsterOne.objects.all().values()
    print(e[1].name)
    
    MonsterOne.objects.create(name="Christmas Orc", style="humanoid", attacks=v, number_attacks=3)

    return HttpResponse(len(v))

# Create your views here.
