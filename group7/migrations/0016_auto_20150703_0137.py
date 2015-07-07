# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('group6', '0002_auto_20150621_1714'),
        ('group7', '0015_auto_20150703_0137'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Date', models.DateField()),
                ('name', models.CharField(max_length=200)),
                ('Projectg7', models.ForeignKey(to='group6.ProjectG6')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Orderinfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Item_name', models.CharField(max_length=200)),
                ('Amount', models.IntegerField(default=0)),
                ('Cost', models.IntegerField(default=0)),
                ('Cost_total', models.IntegerField(default=0)),
                ('OrderID', models.CharField(max_length=200, null=True)),
                ('Company', models.CharField(max_length=200)),
                ('Order', models.ForeignKey(to='group7.Order')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Requisition',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Date', models.DateField()),
                ('Requisition_Id', models.CharField(max_length=200)),
                ('Moreabout', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Status_Of',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Date', models.DateField()),
                ('State', models.CharField(max_length=200)),
                ('Status', models.CharField(max_length=200)),
                ('Moreabout', models.CharField(max_length=200, null=True)),
                ('Prove', models.CharField(max_length=200)),
                ('Order', models.ForeignKey(to='group7.Order')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='requisition',
            name='Status_of',
            field=models.ForeignKey(to='group7.Status_Of'),
            preserve_default=True,
        ),
    ]
