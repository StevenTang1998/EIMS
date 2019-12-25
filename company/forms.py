from django import forms
from .models import Company, Change, Trademark, Classification


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'
        labels = {
            'uniform_social_credit_code': '统一社会信用代码',
            'name': '企业名称',
            'registered_capital': '注册资本',
            'paid_up_capital': '实缴资本',
            'business_scope': '经营范围',
            'industry': '所属行业',
            'tel': '电话',
            'email': '邮箱',
            'province': '省',
            'city': '市',
            'district': '县/区',
            'detail_address': '详细地址',
            'company_type': '企业类型',
            'business_registration_number': '工商注册号',
            'registration_authority': '登记机关',
            'operating_status': '经营状态',
        }
        widgets = {
            'uniform_social_credit_code': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'registered_capital': forms.TextInput(attrs={'class': 'form-control'}),
            'paid_up_capital': forms.TextInput(attrs={'class': 'form-control'}),
            'business_scope': forms.TextInput(attrs={'class': 'form-control'}),
            'industry': forms.TextInput(attrs={'class': 'form-control'}),
            'tel': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'province': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'district': forms.TextInput(attrs={'class': 'form-control'}),
            'detail_address': forms.TextInput(attrs={'class': 'form-control'}),
            'company_type': forms.TextInput(attrs={'class': 'form-control'}),
            'business_registration_number': forms.TextInput(attrs={'class': 'form-control'}),
            'registration_authority': forms.TextInput(attrs={'class': 'form-control'}),
            'operating_status': forms.TextInput(attrs={'class': 'form-control'}),
        }
