# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_auto_20150630_1201'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='ext',
            field=models.CharField(max_length=10, blank=True),
            preserve_default=True,
        ),
    ]
