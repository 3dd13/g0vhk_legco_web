# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-22 09:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('legco', '0014_auto_20160721_0623'),
    ]

    operations = [
        migrations.CreateModel(
            name='FinanceMeetingItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=2048)),
                ('source', models.CharField(max_length=2048)),
                ('keywords', models.ManyToManyField(to='legco.Keyword')),
            ],
        ),
        migrations.CreateModel(
            name='FinanceMeetingItemEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('decision', models.CharField(max_length=128)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='legco.FinanceMeetingItem')),
                ('vote', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='legco.Vote')),
            ],
        ),
        migrations.CreateModel(
            name='FinanceMeetingResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=128, unique=True)),
                ('source', models.CharField(max_length=2048)),
                ('meeting', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='legco.Meeting')),
            ],
        ),
    ]
