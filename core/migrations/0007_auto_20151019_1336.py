# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20151019_1335'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='alcohol',
        ),
        migrations.RemoveField(
            model_name='location',
            name='bathrooms',
        ),
        migrations.RemoveField(
            model_name='location',
            name='coffee',
        ),
        migrations.RemoveField(
            model_name='location',
            name='food',
        ),
        migrations.RemoveField(
            model_name='location',
            name='outdoor',
        ),
        migrations.RemoveField(
            model_name='location',
            name='outlets',
        ),
        migrations.RemoveField(
            model_name='location',
            name='seating',
        ),
        migrations.RemoveField(
            model_name='location',
            name='wifi',
        ),
    ]
