# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20150621_1618'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='birthDate',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='blood_type',
            field=models.CharField(default=django.utils.timezone.now, max_length=2, choices=[(b'0', b'O'), (b'1', b'A'), (b'2', b'B'), (b'3', b'AB')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='degree',
            field=models.CharField(default=django.utils.timezone.now, max_length=1, choices=[(b'0', b'\xe0\xb8\x9b\xe0\xb8\xa3\xe0\xb8\xb4\xe0\xb8\x8d\xe0\xb8\x8d\xe0\xb8\xb2\xe0\xb8\x95\xe0\xb8\xa3\xe0\xb8\xb5'), (b'1', b'\xe0\xb8\x9b\xe0\xb8\xa3\xe0\xb8\xb4\xe0\xb8\x8d\xe0\xb8\x8d\xe0\xb8\xb2\xe0\xb9\x82\xe0\xb8\x97'), (b'2', b'\xe0\xb8\x9b\xe0\xb8\xa3\xe0\xb8\xb4\xe0\xb8\x8d\xe0\xb8\x8d\xe0\xb8\xb2\xe0\xb9\x80\xe0\xb8\xad\xe0\xb8\x81')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='id_number',
            field=models.CharField(default=django.utils.timezone.now, max_length=13),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='nationality',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='religion',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='sex',
            field=models.CharField(default=django.utils.timezone.now, max_length=1, choices=[(b'0', b'\xe0\xb8\x8a\xe0\xb8\xb2\xe0\xb8\xa2'), (b'1', b'\xe0\xb8\xab\xe0\xb8\x8d\xe0\xb8\xb4\xe0\xb8\x87')]),
            preserve_default=False,
        ),
    ]
