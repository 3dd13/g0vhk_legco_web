# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-22 14:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('legco', '0016_financemeetingitem_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='financemeetingitemevent',
            name='result',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='legco.FinanceMeetingResult'),
        ),
    ]