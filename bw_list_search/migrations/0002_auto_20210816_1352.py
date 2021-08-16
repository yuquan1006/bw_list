# Generated by Django 3.2.6 on 2021-08-16 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bw_list_search', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bw_list',
            name='status',
            field=models.IntegerField(choices=[(-1, '未审核'), (0, '已审核')]),
        ),
        migrations.AlterField(
            model_name='bw_list',
            name='type',
            field=models.IntegerField(choices=[(-1, '黑'), (0, '白')]),
        ),
    ]
