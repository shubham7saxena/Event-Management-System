# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registeration', '0002_auto_20160307_1210'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventuserregistration',
            name='event',
        ),
        migrations.RemoveField(
            model_name='eventuserregistration',
            name='user',
        ),
        migrations.DeleteModel(
            name='EventUserRegistration',
        ),
    ]
