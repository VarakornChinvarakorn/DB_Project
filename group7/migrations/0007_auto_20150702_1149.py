# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('group7', '0006_orderinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderinfo',
            name='Image',
            field=models.FileField(upload_to=b'./documents'),
            preserve_default=True,
        ),
    ]
