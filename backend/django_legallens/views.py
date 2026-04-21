from django.shortcuts import render
from django.views.generic import ListView

class HomeDashboard(ListView):

    model = None
    template_name = 'HomeDashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context

