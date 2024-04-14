from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("shorten_url", views.shorten_url, name="shorten_url"),
    path("<slug:token>", views.redirect_url, name="redirect_url"),
]
