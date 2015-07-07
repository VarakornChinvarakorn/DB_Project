# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_userprofile_ext'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('Course_ID', models.IntegerField(max_length=10, serialize=False, primary_key=True)),
                ('Course_Name', models.CharField(max_length=100)),
                ('Credit', models.CharField(max_length=10)),
                ('Describe', models.CharField(max_length=1000, blank=True)),
                ('Course_Before', models.IntegerField(max_length=10, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('Department_ID', models.IntegerField(max_length=10, serialize=False, primary_key=True)),
                ('Department_Name', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('year', models.IntegerField(max_length=10)),
                ('term', models.IntegerField(max_length=1)),
                ('Grade', models.CharField(max_length=1, choices=[(b'0', b'F'), (b'1', b'D'), (b'2', b'D+'), (b'3', b'C'), (b'4', b'C+'), (b'5', b'B'), (b'6', b'B+'), (b'7', b'A'), (b'8', b'FA'), (b'9', b'I')])),
                ('Course_ID', models.ForeignKey(to='group2.Course')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='scheme',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('scheme', models.CharField(max_length=1, choices=[(b'0', b'\xe0\xb8\xab\xe0\xb8\xa5\xe0\xb8\xb1\xe0\xb8\x81\xe0\xb8\xaa\xe0\xb8\xb9\xe0\xb8\x95\xe0\xb8\xa3\xe0\xb8\x9b\xe0\xb8\xa3\xe0\xb8\xb1\xe0\xb8\x9a\xe0\xb8\x9b\xe0\xb8\xa3\xe0\xb8\xb8\xe0\xb8\x87 Cpr.E 54'), (b'1', b'\xe0\xb8\xab\xe0\xb8\xa5\xe0\xb8\xb1\xe0\xb8\x81\xe0\xb8\xaa\xe0\xb8\xb9\xe0\xb8\x95\xe0\xb8\xa3\xe0\xb8\x9b\xe0\xb8\xa3\xe0\xb8\xb1\xe0\xb8\x9a\xe0\xb8\x9b\xe0\xb8\xa3\xe0\xb8\xb8\xe0\xb8\x87 EE 51'), (b'2', b'\xe0\xb8\xab\xe0\xb8\xa5\xe0\xb8\xb1\xe0\xb8\x81\xe0\xb8\xaa\xe0\xb8\xb9\xe0\xb8\x95\xe0\xb8\xa3\xe0\xb8\x9b\xe0\xb8\xa3\xe0\xb8\xb1\xe0\xb8\x9a\xe0\xb8\x9b\xe0\xb8\xa3\xe0\xb8\xb8\xe0\xb8\x87 ECE 55')])),
                ('Course_ID', models.ForeignKey(to='group2.Course')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('Section', models.IntegerField(max_length=7, serialize=False, primary_key=True)),
                ('classroom', models.CharField(max_length=20)),
                ('startTime', models.TimeField()),
                ('endTime', models.TimeField()),
                ('date', models.CharField(max_length=1, choices=[(b'M', b'Monday'), (b'T', b'Tuesday'), (b'W', b'Wednesday'), (b'H', b'Thursday'), (b'F', b'Friday'), (b'S', b'Saturday')])),
                ('Course_ID', models.ForeignKey(to='group2.Course')),
                ('Teacher_ID', models.ForeignKey(to='login.Teacher')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Teacher_Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Course_ID', models.ForeignKey(to='group2.Course')),
                ('Section', models.ForeignKey(to='group2.Section')),
                ('shortname', models.ForeignKey(to='login.Teacher')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='grade',
            name='Section',
            field=models.ForeignKey(to='group2.Section'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='grade',
            name='std_id',
            field=models.ForeignKey(to='login.Student'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='course',
            name='Department_ID',
            field=models.ForeignKey(to='group2.Department'),
            preserve_default=True,
        ),
    ]
