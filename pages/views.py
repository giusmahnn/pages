from django.shortcuts import render
from django.views.generic import TemplateView  #Template view is a django built-in template content
# Create your views here.


class HomePage(TemplateView):
    template_name = 'home.html'   # specify the name of our html the view is to control



class AboutPage(TemplateView):
    template_name = 'about.html'    # specify the name of our html the view is to control