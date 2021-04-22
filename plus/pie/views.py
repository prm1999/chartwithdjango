from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Showchart


class ShowchartView(TemplateView):
    template_name='pie/pie.html'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["qs"]=Showchart.objects.all()
        return context


