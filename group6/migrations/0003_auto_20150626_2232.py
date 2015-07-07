# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('group6', '0002_auto_20150621_1714'),
    ]

    operations = [
        migrations.CreateModel(
            name='StepInTimeLine',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('processDescription', models.CharField(max_length=200)),
                ('month1', models.BooleanField(default=0)),
                ('month2', models.BooleanField(default=0)),
                ('month3', models.BooleanField(default=0)),
                ('month4', models.BooleanField(default=0)),
                ('month5', models.BooleanField(default=0)),
                ('month6', models.BooleanField(default=0)),
                ('month7', models.BooleanField(default=0)),
                ('month8', models.BooleanField(default=0)),
                ('month9', models.BooleanField(default=0)),
                ('month10', models.BooleanField(default=0)),
                ('month11', models.BooleanField(default=0)),
                ('month12', models.BooleanField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TimeLineForm',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('day', models.IntegerField(default=1)),
                ('month', models.CharField(max_length=200)),
                ('year', models.IntegerField(default=1)),
                ('note', models.TextField()),
                ('project', models.ForeignKey(to='group6.ProjectG6')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='stepintimeline',
            name='timeline',
            field=models.ForeignKey(to='group6.TimeLineForm'),
            preserve_default=True,
        ),
    ]
