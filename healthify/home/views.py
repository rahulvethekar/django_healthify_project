from django.shortcuts import render,redirect
from django.views.generic.base import TemplateView

# Create your views here.

class HomeView(TemplateView):

    template_name = 'home/home.html'