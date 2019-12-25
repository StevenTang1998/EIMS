from django.db import models


class Company(models.Model):
    uniform_social_credit_code = models.CharField(max_length=18)
    name = models.CharField(max_length=128)
    registered_capital = models.CharField(max_length=64)
    paid_up_capital = models.CharField(max_length=64)
    business_scope = models.CharField(max_length=1024)
    industry = models.CharField(max_length=128)
    tel = models.CharField(max_length=64)
    email = models.EmailField()
    province = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
    district = models.CharField(max_length=32)
    detail_address = models.CharField(max_length=128)
    company_type = models.CharField(max_length=128)
    business_registration_number = models.CharField(max_length=14)
    registration_authority = models.CharField(max_length=128)
    operating_status = models.CharField(max_length=64)


class Change(models.Model):
    company = models.ForeignKey('Company', on_delete=models.CASCADE)
    change_date = models.DateField()
    change_item = models.CharField(max_length=64)
    before_change = models.CharField(max_length=1024)
    after_change = models.CharField(max_length=1024)
    create_date = models.DateField(auto_now_add=True)


class Trademark(models.Model):
    id = models.CharField(max_length=16, primary_key=True)
    company = models.ForeignKey('Company', on_delete=models.CASCADE)
    image_url = models.URLField()
    name = models.CharField(max_length=128)


class Classification(models.Model):
    trademark = models.ForeignKey('Trademark', on_delete=models.CASCADE)
    classification = models.CharField(max_length=64)
    process = models.CharField(max_length=64)
    status = models.CharField(max_length=16)
