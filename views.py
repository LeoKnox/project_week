from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import Weapon, Spell

# Create your views here.
def index(request):
    return HttpResponse('start here')

def create(request):

    return render(request, "sup_app/creation.html")

def create_weapon(request):
    errors = Weapon.objects.weapon_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/create")
    else:
        Weapon.objects.create(weapon=request.POST["weapon"],number=request.POST["number"],dice=request.POST["dice"],equip=request.POST["equip"])
    return redirect("/main")

def create_spell(request):
    errors = Spell.objects.spell_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/create")
    else:
        print('spells')
    return redirect("/main")

def main(request):
    content= {
        "arsenal":Weapon.objects.all()
    }
    return render(request, "sup_app/main.html", content)