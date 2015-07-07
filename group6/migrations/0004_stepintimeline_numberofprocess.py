# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('group6', '0003_auto_20150626_2232'),
    ]

    operations = [
        migrations.AddField(
            model_name='stepintimeline',
            name='numberOfProcess',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
    ]
