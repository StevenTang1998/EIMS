from django.db import models


class Serving(models.Model):
    company = models.ForeignKey('company.Company', verbose_name='所属企业', on_delete=models.CASCADE)
    human_name = models.CharField('姓名', max_length=32, db_index=True)
    position = models.CharField('职位', max_length=32)

    def __str__(self):
        return self.human_name

    class Meta:
        verbose_name = '主要人员'
        verbose_name_plural = '主要人员'
