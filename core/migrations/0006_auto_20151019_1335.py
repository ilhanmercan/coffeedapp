# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20151019_1323'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='weed',
            new_name='coffee',
        ),
    ]
