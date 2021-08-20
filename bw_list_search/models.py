from django.db import models


# Create your models here.
class Bw_list(models.Model):
    company_name = models.CharField('公司名称', null=True, max_length=256)
    choices_type = [
        (-1, '黑'),
        (0, '白')
    ]
    choices_status = [
        (-1, '未审核'),
        (0, '已审核')
    ]
    type = models.IntegerField(choices=choices_type)
    status = models.IntegerField(choices=choices_status)
    update_time = models.DateTimeField('更新时间', null=True,blank=True)
    detail = models.CharField('详细信息', max_length=260, default="", blank=True)
    class Meta:
        verbose_name = '黑白名单'
        verbose_name_plural = "黑白名单"