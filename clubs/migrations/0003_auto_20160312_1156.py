# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-12 11:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0002_auto_20160312_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='club',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='players', to='clubs.Club'),
        ),
    ]
