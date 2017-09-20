# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfis', '0002_auto_20170920_0500'),
    ]

    operations = [
        migrations.CreateModel(
            name='Convite',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('convidado', models.ForeignKey(to='perfis.Perfil', related_name='convites_recebidos')),
                ('solicitante', models.ForeignKey(to='perfis.Perfil', related_name='convites_feitos')),
            ],
        ),
    ]
