# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-07 18:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registeration', '0006_auto_20160307_0826'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='first_day_preference',
            field=models.CharField(choices=[(b'0', b'Day 1'), (b'1', b'Day 2'), (b'2', b'Day 3'), (b'3', b'Day 4')], default=b'0', max_length=2),
        ),
        migrations.AddField(
            model_name='event',
            name='second_day_preference',
            field=models.CharField(choices=[(b'0', b'Day 1'), (b'1', b'Day 2'), (b'2', b'Day 3'), (b'3', b'Day 4')], default=b'1', max_length=2),
        ),
        migrations.AddField(
            model_name='event',
            name='third_day_preference',
            field=models.CharField(choices=[(b'0', b'Day 1'), (b'1', b'Day 2'), (b'2', b'Day 3'), (b'3', b'Day 4')], default=b'2', max_length=2),
        ),
        migrations.AlterField(
            model_name='event',
            name='first_time_preference',
            field=models.CharField(choices=[(b'0', b'9:00 a.m.'), (b'1', b'10:00 a.m.'), (b'2', b'11:00 a.m.'), (b'3', b'12:00 a.m.'), (b'4', b'1:00 p.m.'), (b'5', b'2:00 p.m.'), (b'6', b'3:00 p.m.'), (b'7', b'4:00 a.m.'), (b'8', b'5:00 p.m.'), (b'9', b'6:00 p.m.')], default=b'0', max_length=2),
        ),
        migrations.AlterField(
            model_name='event',
            name='second_time_preference',
            field=models.CharField(choices=[(b'0', b'9:00 a.m.'), (b'1', b'10:00 a.m.'), (b'2', b'11:00 a.m.'), (b'3', b'12:00 a.m.'), (b'4', b'1:00 p.m.'), (b'5', b'2:00 p.m.'), (b'6', b'3:00 p.m.'), (b'7', b'4:00 a.m.'), (b'8', b'5:00 p.m.'), (b'9', b'6:00 p.m.')], default=b'1', max_length=2),
        ),
        migrations.AlterField(
            model_name='event',
            name='third_time_preference',
            field=models.CharField(choices=[(b'0', b'9:00 a.m.'), (b'1', b'10:00 a.m.'), (b'2', b'11:00 a.m.'), (b'3', b'12:00 a.m.'), (b'4', b'1:00 p.m.'), (b'5', b'2:00 p.m.'), (b'6', b'3:00 p.m.'), (b'7', b'4:00 a.m.'), (b'8', b'5:00 p.m.'), (b'9', b'6:00 p.m.')], default=b'2', max_length=2),
        ),
    ]
