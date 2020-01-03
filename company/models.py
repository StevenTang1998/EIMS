from django.db import models


class Company(models.Model):
    uniform_social_credit_code = models.CharField('统一社会信用代码', max_length=18)
    name = models.CharField('企业名称', max_length=128)
    registered_capital = models.IntegerField('注册资本', db_index=True, null=True)
    paid_up_capital = models.IntegerField('实缴资本', null=True)
    business_scope = models.CharField('经营范围', max_length=1024, null=True)
    industry = models.CharField('所属行业', max_length=128, db_index=True, null=True)
    tel = models.CharField('电话', max_length=64, null=True)
    email = models.EmailField('邮箱', null=True)
    province = models.CharField('省', max_length=32, db_index=True, null=True)
    city = models.CharField('市', max_length=32, null=True)
    district = models.CharField('县/区', max_length=32, null=True)
    detail_address = models.CharField('详细地址', max_length=128, null=True)
    company_type = models.CharField('企业类型', max_length=128, null=True)
    business_registration_number = models.CharField('工商注册号', max_length=14, null=True)
    registration_authority = models.CharField('登记机关', max_length=128, null=True)
    operating_status = models.CharField('经营范围', max_length=64, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '企业基础信息'
        verbose_name_plural = '企业基础信息'


class Change(models.Model):
    company = models.ForeignKey('Company', verbose_name='所属企业', on_delete=models.CASCADE)
    change_date = models.DateField('变更时间')
    change_item = models.CharField('变更项目', max_length=256)
    before_change = models.CharField('变更前', max_length=1024)
    after_change = models.CharField('变更后', max_length=1024)
    create_date = models.DateField('创建时间', auto_now_add=True)

    def __str__(self):
        return self.company.name + ' ' + self.change_item

    class Meta:
        verbose_name = '企业变更信息'
        verbose_name_plural = '企业变更信息'


class Trademark(models.Model):
    id = models.CharField(max_length=16, primary_key=True)
    company = models.ForeignKey('Company', verbose_name='所属企业', on_delete=models.CASCADE)
    image_url = models.URLField('商标')
    name = models.CharField('商标名称', max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '商标注册'
        verbose_name_plural = '商标注册'


class Classification(models.Model):
    trademark = models.ForeignKey('Trademark', verbose_name='商标名称', on_delete=models.CASCADE)
    classification = models.CharField('国际分类', max_length=64)
    process = models.CharField('商标流程', max_length=64)
    status = models.CharField('商标状态', max_length=16)

    def __str__(self):
        return self.trademark.name + ' ' + self.classification

    class Meta:
        verbose_name = '商标分类信息'
        verbose_name_plural = '商标分类信息'
