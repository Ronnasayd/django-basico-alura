# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('perfis', '0004_perfil_contatos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfil',
            name='email',
        ),
        migrations.AddField(
            model_name='perfil',
            name='usuario',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL, default=1, related_name='perfil'),
            preserve_default=False,
        ),
    ]
