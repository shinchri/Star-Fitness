from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from django.views import generic

# Create your views here.
class MainView(generic.TemplateView):
  template_name = 'main/main.html'