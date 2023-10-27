from typing import Any
from django.shortcuts import render
from django.views import generic
from . import models


class IndexView(generic.TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tasks = models.Task.objects.all().order_by('due_date')
        context['tasks'] = tasks
        return context