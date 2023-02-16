# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2022-11-29 18:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Eid', models.IntegerField()),
                ('Ename', models.CharField(max_length=30)),
                ('Esal', models.FloatField()),
                ('Design', models.CharField(max_length=30)),
                ('Company', models.CharField(max_length=30)),
                ('Join_Date', models.DateField()),
                ('Location', models.CharField(max_length=30)),
            ],
        ),
    ]
