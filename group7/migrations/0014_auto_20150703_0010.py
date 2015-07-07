# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('group7', '0013_auto_20150702_2344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderinfo',
            name='Order',
            field=models.ForeignKey(to='group7.Company'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='status_of',
            name='Order',
            field=models.ForeignKey(to='group7.Order'),
            preserve_default=True,
        ),
    ]
