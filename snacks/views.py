from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import snack

# Create your views here.
class HomePage(TemplateView):
    template_name='home.html'

class AboutPage(TemplateView):
    template_name='about.html'

class SnackListView(ListView):
    model=snack
    template_name='snack_list.html'

class SnackDetails(DetailView):
    model=snack
    template_name='snack_details.html'