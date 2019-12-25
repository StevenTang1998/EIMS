from django.shortcuts import render
from .models import Serving


def human(request, name):
    serving = Serving.objects.filter(human_name=name)
    return render(request, 'human.html', locals())
