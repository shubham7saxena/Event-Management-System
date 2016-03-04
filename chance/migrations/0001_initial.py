# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import chance.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255, null=True, blank=True)),
                ('starts', models.DateTimeField()),
                ('ends', models.DateTimeField()),
                ('registration_limit', models.PositiveSmallIntegerField(default=0, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='EventChoice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', models.PositiveIntegerField(default=0)),
                ('name', models.CharField(max_length=32, validators=[chance.models.validate_choice_name])),
                ('label', models.CharField(max_length=255)),
                ('description', models.TextField(null=True, blank=True)),
                ('required', models.BooleanField(default=False)),
                ('allow_multiple', models.BooleanField(default=False)),
                ('event', models.ForeignKey(related_name='choices', to='chance.Event')),
            ],
            options={
                'ordering': ('order',),
            },
        ),
        migrations.CreateModel(
            name='EventChoiceOption',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', models.PositiveIntegerField(default=0)),
                ('display', models.CharField(max_length=128)),
                ('enabled', models.BooleanField(default=True)),
                ('choice', models.ForeignKey(related_name='options', to='chance.EventChoice')),
            ],
            options={
                'ordering': ('order',),
            },
        ),
        migrations.CreateModel(
            name='EventChoiceSelection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('option', models.ForeignKey(related_name='+', to='chance.EventChoiceOption')),
            ],
        ),
        migrations.CreateModel(
            name='EventFee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('available', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=255)),
                ('amount', models.DecimalField(max_digits=255, decimal_places=2)),
                ('event', models.ForeignKey(related_name='fee_options', to='chance.Event')),
            ],
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('attendee_name', models.CharField(max_length=255)),
                ('attendee_email', models.EmailField(max_length=254)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('paid', models.BooleanField(default=False)),
                ('event', models.ForeignKey(related_name='registrations', to='chance.Event')),
                ('fee_option', models.ForeignKey(related_name='+', blank=True, to='chance.EventFee', null=True)),
                ('owner', models.ForeignKey(related_name='+', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
        migrations.AddField(
            model_name='eventchoiceselection',
            name='registration',
            field=models.ForeignKey(related_name='selections', to='chance.Registration'),
        ),
        migrations.AlterUniqueTogether(
            name='eventchoice',
            unique_together=set([('name', 'event')]),
        ),
    ]
