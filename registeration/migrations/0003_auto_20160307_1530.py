# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registeration', '0002_auto_20160307_1501'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='first_name',
            field=models.TextField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='last_name',
            field=models.TextField(max_length=20, null=True, blank=True),
        ),
    ]
