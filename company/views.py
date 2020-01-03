from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from .models import Company
from django.db.models import Q


entry_per_page = 20


def search_company(request, name, province, industry, capital, company_type, operating_status, page):
    if request.method == 'GET' and name:
        query = Q(name__contains=name)
        if province != '不限':
            query &= Q(province=province)
        if industry != '不限':
            query &= Q(industry=industry)
        if capital != '不限':
            capital = int(capital)
            print(capital)
            if capital == 0:
                query &= Q(registered_capital__lt=100)
            elif capital == 1:
                query &= Q(registered_capital__gte=100) & Q(registered_capital__lt=200)
            elif capital == 2:
                query &= Q(registered_capital__gte=200) & Q(registered_capital__lt=500)
            elif capital == 3:
                query &= Q(registered_capital__gte=500) & Q(registered_capital__lt=1000)
            elif capital == 4:
                query &= Q(registered_capital__gte=1000)
        if company_type != '不限':
            query &= Q(company_type=company_type)
        if operating_status != '不限':
            query &= Q(operating_status=operating_status)
        total_company_list = Company.objects.filter(query)
        company_count = total_company_list.count()
        total_page = (company_count + entry_per_page - 1) // entry_per_page
        page = max(min(page, total_page), 1)
        company_list = total_company_list[(page - 1) * entry_per_page: page * entry_per_page]
        pre_page, next_page = page - 1, page + 1
        if total_page < 5:
            page_list = list(range(1, total_page + 1))
        else:
            left, right = page - 1, total_page - page
            left, right = min(left, 2 + max(0, 2 - right)), min(right, 2 + max(0, 2 - left))
            page_list = list(range(page - left, page + right + 1))
        return render(request, 'search_company.html', locals())
    else:
        return redirect('/')


def company_detail(request, pk):
    company = get_object_or_404(Company, pk=pk)
    model = Company
    return render(request, 'company.html', locals())
