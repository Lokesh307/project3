from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def siva(request):
    return HttpResponse('<h1>Siva is Topper</h1>')


def naveen(request):
    return HttpResponse('<h1>Naveen is Mental Boy</h1>')