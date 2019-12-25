from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from .models import Company, Change, Trademark, Classification
from .forms import CompanyForm
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
            pass
        if company_type != '不限':
            query &= Q(company_type=company_type)
        if operating_status != '不限':
            query &= Q(operating_status=operating_status)
        company_count = Company.objects.filter(query).count()
        company_list = Company.objects.filter(query)[(page - 1) * entry_per_page: page * entry_per_page]
        total_page = (company_count + entry_per_page - 1) // entry_per_page
        page = min(max(page, 1), total_page)
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
    return render(request, 'company.html', locals())
