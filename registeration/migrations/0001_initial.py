# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('first_time_preference', models.CharField(default=b'1', max_length=2, choices=[(b'01', b'Day 1, 9:00am'), (b'02', b'Day 1, 11:00am'), (b'03', b'Day 1, 1:00pm'), (b'04', b'Day 1, 3:00pm'), (b'05', b'Day 1, 5:00pm'), (b'11', b'Day 2, 9:00am'), (b'12', b'Day 2, 11:00am'), (b'13', b'Day 2, 1:00pm'), (b'14', b'Day 2, 3:00pm'), (b'15', b'Day 2, 5:00pm')])),
                ('second_time_preference', models.CharField(default=b'2', max_length=2, choices=[(b'01', b'Day 1, 9:00am'), (b'02', b'Day 1, 11:00am'), (b'03', b'Day 1, 1:00pm'), (b'04', b'Day 1, 3:00pm'), (b'05', b'Day 1, 5:00pm'), (b'11', b'Day 2, 9:00am'), (b'12', b'Day 2, 11:00am'), (b'13', b'Day 2, 1:00pm'), (b'14', b'Day 2, 3:00pm'), (b'15', b'Day 2, 5:00pm')])),
                ('third_time_preference', models.CharField(default=b'3', max_length=2, choices=[(b'01', b'Day 1, 9:00am'), (b'02', b'Day 1, 11:00am'), (b'03', b'Day 1, 1:00pm'), (b'04', b'Day 1, 3:00pm'), (b'05', b'Day 1, 5:00pm'), (b'11', b'Day 2, 9:00am'), (b'12', b'Day 2, 11:00am'), (b'13', b'Day 2, 1:00pm'), (b'14', b'Day 2, 3:00pm'), (b'15', b'Day 2, 5:00pm')])),
                ('event_coordi', models.CharField(max_length=50)),
                ('contact_id_coordinator', models.EmailField(max_length=254)),
                ('event_description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='EventUserRegistration',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('event', models.ForeignKey(to='registeration.Event')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('website', models.URLField(blank=True)),
                ('picture', models.ImageField(upload_to=b'profile_images', blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='eventuserregistration',
            name='user',
            field=models.ForeignKey(to='registeration.Profile'),
        ),
        migrations.AddField(
            model_name='event',
            name='participants',
            field=models.ManyToManyField(to='registeration.Profile'),
        ),
    ]
