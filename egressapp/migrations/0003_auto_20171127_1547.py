# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-27 15:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('egressapp', '0002_aluno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='cpf',
            field=models.CharField(max_length=11),
        ),
    ]
