# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registeration', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='participants',
            new_name='participant',
        ),
    ]
