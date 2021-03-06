# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-04-19 06:40
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pcari', '0074_auto_20180417_0207'),
    ]

    operations = [
        migrations.RenameField(
            model_name='respondent',
            old_name='PPiI',
            new_name='PPiIAge',
        ),
        migrations.RenameField(
            model_name='respondent',
            old_name='PPiII',
            new_name='PPiIIAge',
        ),
        migrations.RenameField(
            model_name='respondent',
            old_name='PPiIII',
            new_name='PPiIIIAge',
        ),
        migrations.RenameField(
            model_name='respondent',
            old_name='PPiIV',
            new_name='PPiIIIName',
        ),
        migrations.RenameField(
            model_name='respondent',
            old_name='PPiIX',
            new_name='PPiIIIQI',
        ),
        migrations.RenameField(
            model_name='respondent',
            old_name='PPiV',
            new_name='PPiIIIQII',
        ),
        migrations.RenameField(
            model_name='respondent',
            old_name='PPiVI',
            new_name='PPiIIIQIII',
        ),
        migrations.RenameField(
            model_name='respondent',
            old_name='PPiVII',
            new_name='PPiIIIQIV',
        ),
        migrations.RenameField(
            model_name='respondent',
            old_name='PPiVIII',
            new_name='PPiIIName',
        ),
        migrations.RenameField(
            model_name='respondent',
            old_name='PPiX',
            new_name='PPiIIQI',
        ),
        migrations.AddField(
            model_name='respondent',
            name='PPiIGender',
            field=models.CharField(blank=True, choices=[('', '(Empty)'), ('M', 'Male'), ('F', 'Female')], default='', max_length=1, validators=[django.core.validators.RegexValidator('^(|M|F)$')]),
        ),
        migrations.AddField(
            model_name='respondent',
            name='PPiIIGender',
            field=models.CharField(blank=True, choices=[('', '(Empty)'), ('M', 'Male'), ('F', 'Female')], default='', max_length=1, validators=[django.core.validators.RegexValidator('^(|M|F)$')]),
        ),
        migrations.AddField(
            model_name='respondent',
            name='PPiIIIGender',
            field=models.CharField(blank=True, choices=[('', '(Empty)'), ('M', 'Male'), ('F', 'Female')], default='', max_length=1, validators=[django.core.validators.RegexValidator('^(|M|F)$')]),
        ),
        migrations.AddField(
            model_name='respondent',
            name='PPiIIQII',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
        migrations.AddField(
            model_name='respondent',
            name='PPiIIQIII',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
        migrations.AddField(
            model_name='respondent',
            name='PPiIIQIV',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
        migrations.AddField(
            model_name='respondent',
            name='PPiIName',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
        migrations.AddField(
            model_name='respondent',
            name='PPiIQI',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
        migrations.AddField(
            model_name='respondent',
            name='PPiIQII',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
        migrations.AddField(
            model_name='respondent',
            name='PPiIQIII',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
        migrations.AddField(
            model_name='respondent',
            name='PPiIQIV',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
        migrations.AddField(
            model_name='respondent',
            name='PPiIVAge',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
        migrations.AddField(
            model_name='respondent',
            name='PPiIVGender',
            field=models.CharField(blank=True, choices=[('', '(Empty)'), ('M', 'Male'), ('F', 'Female')], default='', max_length=1, validators=[django.core.validators.RegexValidator('^(|M|F)$')]),
        ),
        migrations.AddField(
            model_name='respondent',
            name='PPiIVName',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
        migrations.AddField(
            model_name='respondent',
            name='PPiIVQI',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
        migrations.AddField(
            model_name='respondent',
            name='PPiIVQII',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
        migrations.AddField(
            model_name='respondent',
            name='PPiIVQIII',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
        migrations.AddField(
            model_name='respondent',
            name='PPiIVQIV',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
        migrations.AddField(
            model_name='respondent',
            name='PPiIXAge',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
        migrations.AddField(
            model_name='respondent',
            name='PPiIXGender',
            field=models.CharField(blank=True, choices=[('', '(Empty)'), ('M', 'Male'), ('F', 'Female')], default='', max_length=1, validators=[django.core.validators.RegexValidator('^(|M|F)$')]),
        ),
        migrations.AddField(
            model_name='respondent',
            name='PPiIXName',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
        migrations.AddField(
            model_name='respondent',
            name='PPiIXQI',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
        migrations.AddField(
            model_name='respondent',
            name='PPiIXQII',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
        migrations.AddField(
            model_name='respondent',
            name='PPiIXQIII',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
        migrations.AddField(
            model_name='respondent',
            name='PPiIXQIV',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
        migrations.AddField(
            model_name='respondent',
            name='PPiVAge',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
        migrations.AddField(
            model_name='respondent',
            name='PPiVGender',
            field=models.CharField(blank=True, choices=[('', '(Empty)'), ('M', 'Male'), ('F', 'Female')], default='', max_length=1, validators=[django.core.validators.RegexValidator('^(|M|F)$')]),
        ),
        migrations.AddField(
            model_name='respondent',
            name='PPiVIAge',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
        migrations.AddField(
            model_name='respondent',
            name='PPiVIGender',
            field=models.CharField(blank=True, choices=[('', '(Empty)'), ('M', 'Male'), ('F', 'Female')], default='', max_length=1, validators=[django.core.validators.RegexValidator('^(|M|F)$')]),
        ),
        migrations.AddField(
            model_name='respondent',
            name='PPiVIIAge',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
        migrations.AddField(
            model_name='respondent',
            name='PPiVIIGender',
            field=models.CharField(blank=True, choices=[('', '(Empty)'), ('M', 'Male'), ('F', 'Female')], default='', max_length=1, validators=[django.core.validators.RegexValidator('^(|M|F)$')]),
        ),
        migrations.AddField(
            model_name='respondent',
            name='PPiVIIIAge',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
        migrations.AddField(
            model_name='respondent',
            name='PPiVIIIGender',
            field=models.CharField(blank=True, choices=[('', '(Empty)'), ('M', 'Male'), ('F', 'Female')], default='', max_length=1, validators=[django.core.validators.RegexValidator('^(|M|F)$')]),
        ),
        migrations.AddField(
            model_name='respondent',
            name='PPiVIIIName',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
        migrations.AddField(
            model_name='respondent',
            name='PPiVIIIQI',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
        migrations.AddField(
            model_name='respondent',
            name='PPiVIIIQII',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
        migrations.AddField(
            model_name='respondent',
            name='PPiVIIIQIII',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
        migrations.AddField(
            model_name='respondent',
            name='PPiVIIIQIV',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
        migrations.AddField(
            model_name='respondent',
            name='PPiVIIName',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
        migrations.AddField(
            model_name='respondent',
            name='PPiVIIQI',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
        migrations.AddField(
            model_name='respondent',
            name='PPiVIIQII',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
        migrations.AddField(
            model_name='respondent',
            name='PPiVIIQIII',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
        migrations.AddField(
            model_name='respondent',
            name='PPiVIIQIV',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
        migrations.AddField(
            model_name='respondent',
            name='PPiVIName',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
        migrations.AddField(
            model_name='respondent',
            name='PPiVIQI',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
        migrations.AddField(
            model_name='respondent',
            name='PPiVIQII',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
        migrations.AddField(
            model_name='respondent',
            name='PPiVIQIII',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
        migrations.AddField(
            model_name='respondent',
            name='PPiVIQIV',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
        migrations.AddField(
            model_name='respondent',
            name='PPiVName',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
        migrations.AddField(
            model_name='respondent',
            name='PPiVQI',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
        migrations.AddField(
            model_name='respondent',
            name='PPiVQII',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
        migrations.AddField(
            model_name='respondent',
            name='PPiVQIII',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
        migrations.AddField(
            model_name='respondent',
            name='PPiVQIV',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
        migrations.AddField(
            model_name='respondent',
            name='PPiXAge',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
        migrations.AddField(
            model_name='respondent',
            name='PPiXGender',
            field=models.CharField(blank=True, choices=[('', '(Empty)'), ('M', 'Male'), ('F', 'Female')], default='', max_length=1, validators=[django.core.validators.RegexValidator('^(|M|F)$')]),
        ),
        migrations.AddField(
            model_name='respondent',
            name='PPiXName',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
        migrations.AddField(
            model_name='respondent',
            name='PPiXQI',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
        migrations.AddField(
            model_name='respondent',
            name='PPiXQII',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
        migrations.AddField(
            model_name='respondent',
            name='PPiXQIII',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
        migrations.AddField(
            model_name='respondent',
            name='PPiXQIV',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
        migrations.AlterField(
            model_name='comment',
            name='language',
            field=models.CharField(blank=True, choices=[(b'en', 'English')], default='', max_length=8, validators=[django.core.validators.RegexValidator('^(|en)$')]),
        ),
        migrations.AlterField(
            model_name='respondent',
            name='language',
            field=models.CharField(blank=True, choices=[(b'en', 'English')], default='', max_length=8, validators=[django.core.validators.RegexValidator('^(|en)$')]),
        ),
    ]
