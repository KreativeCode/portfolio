from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse

# Create your views here.# Create your views here.
def index(response):
    return render(response, "pages/index.html", {})
