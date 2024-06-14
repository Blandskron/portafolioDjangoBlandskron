from django.shortcuts import render
from .models import HardSkill


def home(request):
    return render(request, 'homeapp/home.html')

def hardskills(request):
    skills = HardSkill.objects.all()
    return render(request, 'homeapp/hardskills.html', {'skills': skills})