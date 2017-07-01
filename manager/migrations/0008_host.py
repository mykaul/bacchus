# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-01 12:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0007_auto_20170429_2014'),
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('hostid', models.CharField(max_length=128, null=True)),
                ('name', models.CharField(max_length=256)),
                ('discovered', models.DateTimeField(editable=False)),
                ('updated', models.DateTimeField()),
                ('cluster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.Cluster')),
            ],
        ),
    ]
