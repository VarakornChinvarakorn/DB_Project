# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('group7', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectg7',
            name='Project',
        ),
        migrations.AlterField(
            model_name='order',
            name='projectg7',
            field=models.ForeignKey(to='group6.ProjectG6'),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='ProjectG7',
        ),
    ]
