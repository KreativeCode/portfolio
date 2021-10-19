from django.urls import path

from . import views

app_name = 'tictactoe'
urlpatterns = [
    path("", views.index, name="index"),
]
