from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Thing

# Create your views here.
class HomePage(TemplateView):
    template_name='home.html'

class AboutPage(TemplateView):
    template_name='about.html'

class SnackListView(ListView):
    template_name='snack_list.html'
    model=Thing

    