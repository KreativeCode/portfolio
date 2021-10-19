from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse

# Create your views here.# Create your views here.
def index(response):
    return render(response, 'tictactoe/index.html', {})
