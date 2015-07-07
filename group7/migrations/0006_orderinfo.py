# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('group7', '0005_auto_20150702_1137'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orderinfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Item_name', models.CharField(max_length=200)),
                ('Amount', models.IntegerField(default=0)),
                ('Cost', models.IntegerField(default=0)),
                ('Cost_total', models.IntegerField(default=0)),
                ('Image', models.FileField(upload_to=b'')),
                ('Order', models.ForeignKey(to='group7.Order')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
