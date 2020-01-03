from django.shortcuts import render
from django.shortcuts import redirect
from .models import Serving
from django.db.models import Q


entry_per_page = 20


def search_human(request, name, position, page):
    if request.method == 'GET' and name:
        query = Q(human_name__contains=name)
        if position != '不限':
            query &= Q(position=position)
        total_human_list = Serving.objects.filter(query).values_list('human_name').distinct()
        human_count = total_human_list.count()
        total_page = (human_count + entry_per_page - 1) // entry_per_page
        page = max(min(page, total_page), 1)
        human_list = total_human_list[(page - 1) * entry_per_page: page * entry_per_page]
        pre_page, next_page = page - 1, page + 1
        if total_page < 5:
            page_list = list(range(1, total_page + 1))
        else:
            left, right = page - 1, total_page - page
            left, right = min(left, 2 + max(0, 2 - right)), min(right, 2 + max(0, 2 - left))
            page_list = list(range(page - left, page + right + 1))
        return render(request, 'search_human.html', locals())
    else:
        return redirect('/')


def human(request, name):
    serving = Serving.objects.filter(human_name=name)
    return render(request, 'human.html', locals())
