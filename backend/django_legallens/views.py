from django.shortcuts import render
from django.views.generic import ListView
from .models import Contract, AuditResult



class HomeDashboard(ListView):

    model = Contract
    template_name = 'HomeDashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context

