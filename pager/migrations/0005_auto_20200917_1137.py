# Generated by Django 2.2.2 on 2020-09-17 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pager', '0004_auto_20200916_0419'),
    ]

    operations = [
        migrations.AddField(
            model_name='speechdata',
            name='date',
            field=models.CharField(default='11/12/2020', max_length=100),
        ),
        migrations.AddField(
            model_name='speechdata',
            name='time',
            field=models.CharField(default='11:20:08 AM', max_length=100),
        ),
    ]
