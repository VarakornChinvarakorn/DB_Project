# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='accept',
            fields=[
                ('No_accept', models.IntegerField(default=0, serialize=False, primary_key=True)),
                ('accept_status', models.CharField(max_length=20)),
                ('Date', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Internship',
            fields=[
                ('name_Internship', models.CharField(max_length=50, serialize=False, primary_key=True)),
                ('add_Internship', models.CharField(max_length=200)),
                ('Tel', models.CharField(max_length=20)),
                ('Fax', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StatusPetition',
            fields=[
                ('NoPetition', models.IntegerField(default=0, serialize=False, primary_key=True)),
                ('StatusPetition', models.CharField(max_length=50)),
                ('Date', models.DateField()),
                ('Date2', models.DateField()),
                ('send', models.CharField(max_length=20)),
                ('Internship', models.ForeignKey(to='group5.Internship')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='studentG5',
            fields=[
                ('studentID', models.CharField(max_length=13, serialize=False, primary_key=True)),
                ('studentYear', models.IntegerField(default=0)),
                ('sex', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='statuspetition',
            name='studentG5',
            field=models.ForeignKey(to='group5.studentG5'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='accept',
            name='StatusPetition',
            field=models.ForeignKey(to='group5.StatusPetition'),
            preserve_default=True,
        ),
    ]
