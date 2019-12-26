from django.db import models


class User(models.Model):
    name = models.CharField('用户名', max_length=128, unique=True)
    password = models.CharField('密码', max_length=128)
    email = models.EmailField('邮箱')
    tel = models.CharField('电话', max_length=32)
    belong = models.ForeignKey('company.Company', verbose_name='所属企业', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '企业用户'
        verbose_name_plural = '企业用户'
