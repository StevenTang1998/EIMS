from django import forms
from captcha.fields import CaptchaField
from captcha.fields import CaptchaTextInput
from .models import User
from company.models import Company
from human.models import Serving


class SearchCompanyForm(forms.Form):
    pass
    # name = forms.CharField(label='名字', max_length=128,
    #                        widget=forms.TextInput(attrs={'class': 'form-control input-lg',
    #                                                      'placeholder': '请输入公司名称',
    #                                                      'autofocus': ''}))
    # province_choice = (('不限', '不限'),) + tuple(Company.objects.all()
    #                                           .values_list('province', 'province')
    #                                           .exclude(province='')
    #                                           .distinct())
    # province = forms.ChoiceField(label='省份地区', choices=province_choice,
    #                              widget=forms.Select(attrs={'class': 'form-control input-lg'}))
    # industry_choice = (('不限', '不限'),) + tuple(Company.objects.all()
    #                                           .values_list('industry', 'industry')
    #                                           .exclude(industry='')
    #                                           .distinct())
    # industry = forms.ChoiceField(label='行业分类', choices=industry_choice,
    #                              widget=forms.Select(attrs={'class': 'form-control input-lg'}))
    # capital_choice = (
    #     ('不限', '不限'),
    #     ('0', '0～100万'),
    #     ('1', '100～200万'),
    #     ('2', '200～500万'),
    #     ('3', '500～1000万'),
    #     ('4', '1000万以上'),
    # )
    # capital = forms.ChoiceField(label='注册资本', choices=capital_choice,
    #                             widget=forms.Select(attrs={'class': 'form-control input-lg'}))
    # company_type_choice = (('不限', '不限'),) + tuple(Company.objects.all()
    #                                               .values_list('company_type', 'company_type')
    #                                               .exclude(company_type='')
    #                                               .distinct())
    # company_type = forms.ChoiceField(label='企业类型', choices=company_type_choice,
    #                                  widget=forms.Select(attrs={'class': 'form-control input-lg'}))
    # operating_status_choice = (('不限', '不限'),) + tuple(Company.objects.all()
    #                                                   .values_list('operating_status', 'operating_status')
    #                                                   .exclude(operating_status='')
    #                                                   .distinct())
    # operating_status = forms.ChoiceField(label='企业经营状况', choices=operating_status_choice,
    #                                      widget=forms.Select(attrs={'class': 'form-control input-lg'}))


class SearchHumanForm(forms.Form):
    pass
    # name = forms.CharField(label='名字', max_length=128,
    #                        widget=forms.TextInput(attrs={'class': 'form-control input-lg',
    #                                                      'placeholder': '请输入老板姓名',
    #                                                      'autofocus': ''}))
    # position_choice = (('不限', '不限'),) + tuple(Serving.objects.all()
    #                                           .values_list('position', 'position')
    #                                           .exclude(position='')
    #                                           .distinct())
    # position = forms.ChoiceField(label='职位', choices=position_choice,
    #                              widget=forms.Select(attrs={'class': 'form-control input-lg'}))


class StatisticForm(forms.Form):
    pass
    # industry_choice = (('不限', '不限'),) + tuple(Company.objects.all()
    #                                           .values_list('industry', 'industry')
    #                                           .exclude(industry='')
    #                                           .distinct())
    # industry = forms.ChoiceField(label='行业分类', choices=industry_choice,
    #                              widget=forms.Select(attrs={'class': 'form-control input-lg'}))
    # province_choice = (('不限', '不限'),) + tuple(Company.objects.all()
    #                                           .values_list('province', 'province')
    #                                           .exclude(province='')
    #                                           .distinct())
    # province = forms.ChoiceField(label='省份地区', choices=province_choice,
    #                              widget=forms.Select(attrs={'class': 'form-control input-lg'}))


class UserForm(forms.Form):
    name = forms.CharField(label='用户名', max_length=128,
                           widget=forms.TextInput(attrs={'class': 'form-control',
                                                         'placeholder': '请输入用户名',
                                                         'autofocus': ''}))
    password = forms.CharField(label='密码', max_length=256,
                               widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                 'placeholder': '请输入密码'}))
    captcha = CaptchaField(label='验证码',
                           widget=CaptchaTextInput(attrs={'class': 'form-control',
                                                          'placeholder': '请输入验证码'}))


class RegisterForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=128,
                               widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'placeholder': '请输入用户名'}))
    password1 = forms.CharField(label='密码', max_length=256,
                                widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                  'placeholder': '请输入密码'}))
    password2 = forms.CharField(label='确认密码', max_length=256,
                                widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                  'placeholder': '请重复输入密码'}))
    email = forms.EmailField(label="邮箱地址",
                             widget=forms.EmailInput(attrs={'class': 'form-control',
                                                            'placeholder': '请输入联系邮箱'}))
    tel = forms.CharField(label='联系电话', max_length=32,
                          widget=forms.TextInput(attrs={'class': 'form-control',
                                                        'placeholder': '请输入联系电话'}))
    captcha = CaptchaField(label='验证码',
                           widget=CaptchaTextInput(attrs={'class': 'form-control',
                                                          'placeholder': '请输入验证码'}))


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('name', 'email', 'tel')
        labels = {
            'name': '用户名',
            'email': '邮箱地址',
            'tel': '联系电话',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control',
                                           'readonly': '',
                                           'placeholder': '请输入用户名'}),
            'email': forms.EmailInput(attrs={'class': 'form-control',
                                             'placeholder': '请输入联系邮箱'}),
            'tel': forms.TextInput(attrs={'class': 'form-control',
                                          'placeholder': '请输入联系电话'}),
        }


class BindForm(forms.Form):
    company_name = forms.CharField(label='绑定公司', max_length=128,
                                   widget=forms.TextInput(attrs={'class': 'form-control',
                                                                 'placeholder': '请输入公司名',
                                                                 'autofocus': ''}))
