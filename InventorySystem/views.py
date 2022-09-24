from django.http import HttpResponse
from django.shortcuts import render

from InventorySystem.models import Customer


# Create your views here.


def index(request):
    return HttpResponse('welcome')