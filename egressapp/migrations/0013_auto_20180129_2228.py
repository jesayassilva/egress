# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-30 01:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('egressapp', '0012_auto_20180111_1815'),
    ]

    operations = [
        migrations.AddField(
            model_name='autorizacaoaluno',
            name='observacoes',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='autorizacaoturma',
            name='observacoes',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]