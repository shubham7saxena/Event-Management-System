# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registeration', '0003_auto_20160307_1254'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='website',
        ),
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=models.TextField(max_length=10, unique=True, null=True),
        ),
    ]
