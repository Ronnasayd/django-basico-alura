# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfis', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='email',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='perfil',
            name='nome',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='perfil',
            name='nome_empresa',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='perfil',
            name='telefone',
            field=models.CharField(default='', max_length=15),
        ),
    ]
