# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registeration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='contact_id_coordinator',
            field=models.EmailField(max_length=254),
        ),
    ]
