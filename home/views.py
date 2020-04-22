from django.shortcuts import render
from django.views.generic import TemplateView
from machine.models import VendingMachine

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
       context = super(HomePageView,self).get_context_data(**kwargs)
       context['machines'] = VendingMachine.objects.all()
       return context