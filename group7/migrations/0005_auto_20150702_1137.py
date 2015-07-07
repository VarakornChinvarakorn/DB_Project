# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('group7', '0004_auto_20150630_1901'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderinfo',
            name='Order',
        ),
        migrations.DeleteModel(
            name='Orderinfo',
        ),
    ]
