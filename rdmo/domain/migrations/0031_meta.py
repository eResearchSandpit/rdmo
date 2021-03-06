# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-04 14:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('domain', '0030_permissions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attribute',
            name='unit',
            field=models.CharField(blank=True, help_text='Unit for this attribute.', max_length=64, null=True, verbose_name='Unit'),
        ),
        migrations.AlterField(
            model_name='attribute',
            name='value_type',
            field=models.CharField(choices=[('text', 'Text'), ('url', 'URL'), ('integer', 'Integer'), ('float', 'Float'), ('boolean', 'Boolean'), ('datetime', 'Datetime'), ('options', 'Options')], help_text='Type of value for this attribute.', max_length=8, verbose_name='Value type'),
        ),
        migrations.AlterField(
            model_name='attributeentity',
            name='key',
            field=models.SlugField(blank=True, help_text='The internal identifier of this attribute/entity.', max_length=128, null=True, verbose_name='Key'),
        ),
    ]
