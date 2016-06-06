# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('revolutionslider', '0005_auto_20150922_1135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='layer',
            name='splitin',
            field=models.CharField(choices=[('', "Don't split"), ('chars', 'Characters'), ('words', 'Words'), ('lines', 'Lines')], max_length=255, blank=True, default=('', "Don't split")),
        ),
        migrations.AlterField(
            model_name='layer',
            name='splitout',
            field=models.CharField(choices=[('', "Don't split"), ('chars', 'Characters'), ('words', 'Words'), ('lines', 'Lines')], max_length=255, blank=True, default=('', "Don't split")),
        ),
    ]
