# Generated by Django 3.2.6 on 2021-08-20 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bw_list_search', '0004_alter_bw_list_detail'),
    ]

    operations = [
        migrations.AddField(
            model_name='bw_list',
            name='update_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='更新时间'),
        ),
    ]
