from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from .models import User
from company.models import Company
from .forms import SearchCompanyForm
from .forms import SearchHumanForm
from .forms import UserForm
from .forms import RegisterForm
from .forms import ProfileForm
from .forms import BindForm
from company.forms import CompanyForm
import hashlib


def hash_code(s, salt='ruc'):
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())
    return h.hexdigest()


def homepage(request):
    if request.method == 'POST':
        search_form = SearchCompanyForm(request.POST)
        if search_form.is_valid():
            # search_type = search_form.cleaned_data.get('search_type')
            name = search_form.cleaned_data.get('name')
            # if search_type == 'company':
            args = (name,
                    search_form.cleaned_data.get('province'),
                    search_form.cleaned_data.get('industry'),
                    search_form.cleaned_data.get('capital'),
                    search_form.cleaned_data.get('company_type'),
                    search_form.cleaned_data.get('operating_status'),
                    1)
            return redirect(reverse('company:search', args=args))
            # else:
            #     return redirect(reverse('human:detail', args=(name,)))
        else:
            return redirect('root')

    search_form = SearchCompanyForm()
    return render(request, 'homepage.html', locals())


def search_human(request):
    if request.method == 'POST':
        search_form = SearchHumanForm(request.POST)
        if search_form.is_valid():
            name = search_form.cleaned_data.get('name')
            args = (name,
                    search_form.cleaned_data.get('position'),
                    1)
            return redirect(reverse('human:search', args=args))
        else:
            return redirect('search_human')

    search_form = SearchHumanForm()
    return render(request, 'homepage_human.html', locals())


def register(request):
    if request.session.get('is_login'):
        return redirect('profile')

    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        message = '请检查填写的内容！'
        if register_form.is_valid():
            username = register_form.cleaned_data.get('username')
            password1 = register_form.cleaned_data.get('password1')
            password2 = register_form.cleaned_data.get('password2')
            email = register_form.cleaned_data.get('email')
            tel = register_form.cleaned_data.get('tel')

            if password1 != password2:
                message = '两次输入的密码不同！'
                return render(request, 'register.html', locals())
            else:
                same_name_user = User.objects.filter(name=username)
                if same_name_user:
                    message = '用户名已经存在'
                    return render(request, 'register.html', locals())
                new_user = User.objects.create(name=username,
                                               password=hash_code(password1),
                                               email=email,
                                               tel=tel)
                return redirect('login')
        else:
            return render(request, 'register.html', locals())
    register_form = RegisterForm()
    return render(request, 'register.html', locals())


def login(request):
    if request.session.get('is_login'):
        return redirect('profile')
    if request.method == 'POST':
        login_form = UserForm(request.POST)
        message = '请检查填写的内容！'
        if login_form.is_valid():
            name = login_form.cleaned_data.get('name')
            password = login_form.cleaned_data.get('password')
            print(name, password)
            try:
                user = User.objects.get(name=name)
            except:
                message = '用户不存在！'
                return render(request, 'login.html', locals())
            if user.password == hash_code(password):
                request.session['is_login'] = True
                request.session['user_id'] = user.id
                request.session['user_name'] = user.name
                return redirect('profile')
            else:
                message = '密码不正确！'
                return render(request, 'login.html', locals())
        else:
            return render(request, 'login.html', locals())

    login_form = UserForm()
    return render(request, 'login.html', locals())


def logout(request):
    if not request.session.get('is_login', None):
        return redirect('login')
    request.session.flush()
    return redirect('login')


def profile(request):
    if not request.session.get('is_login', None):
        return redirect('login')

    user = User.objects.get(id=request.session.get('user_id'))

    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, instance=user)
        message = '请检查填写的内容！'
        if profile_form.is_valid():
            profile_form.save()
            return redirect('profile')
        else:
            return render(request, 'profile.html', locals())

    user = User.objects.get(id=request.session.get('user_id'))
    profile_form = ProfileForm(instance=user)
    return render(request, 'profile.html', locals())


def bind(request):
    if not request.session.get('is_login'):
        return redirect('login')

    user = User.objects.get(id=request.session.get('user_id'))
    if user.belong:
        return redirect('modify')

    if request.method == 'POST':
        bind_form = BindForm(request.POST)
        message = '请检查填写的内容！'
        if bind_form.is_valid():
            company_name = bind_form.cleaned_data.get('company_name')
            try:
                company = Company.objects.get(name=company_name)
                user.belong = company
                user.save()
                return redirect('modify')
            except:
                message = '该公司不存在'
                return render(request, 'bind.html', locals())
        else:
            return render(request, 'bind.html', locals())

    bind_form = BindForm()
    return render(request, 'bind.html', locals())


def modify(request):
    if not request.session.get('is_login'):
        return redirect('login')

    user = User.objects.get(id=request.session.get('user_id'))
    if not user.belong:
        return redirect('bind')

    if request.method == 'POST':
        company_form = CompanyForm(request.POST, instance=user.belong)
        message = '请检查填写的内容！'
        if company_form.is_valid():
            company_form.save()
            message = '修改成功'
    else:
        company_form = CompanyForm(instance=user.belong)

    return render(request, 'modify.html', locals())
