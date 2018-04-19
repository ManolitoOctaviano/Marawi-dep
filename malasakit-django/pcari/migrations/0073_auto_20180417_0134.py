# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-04-17 08:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pcari', '0072_auto_20180415_2358'),
    ]

    operations = [
        migrations.AddField(
            model_name='respondent',
            name='PPI_I',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
        migrations.AddField(
            model_name='respondent',
            name='PPI_II',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
        migrations.AddField(
            model_name='respondent',
            name='PPI_III',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
        migrations.AddField(
            model_name='respondent',
            name='PPI_IV',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
        migrations.AddField(
            model_name='respondent',
            name='PPI_IX',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
        migrations.AddField(
            model_name='respondent',
            name='PPI_V',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
        migrations.AddField(
            model_name='respondent',
            name='PPI_VI',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
        migrations.AddField(
            model_name='respondent',
            name='PPI_VII',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
        migrations.AddField(
            model_name='respondent',
            name='PPI_VIII',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
        migrations.AddField(
            model_name='respondent',
            name='PPI_X',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
        migrations.AddField(
            model_name='respondent',
            name='interviewer',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
    ]