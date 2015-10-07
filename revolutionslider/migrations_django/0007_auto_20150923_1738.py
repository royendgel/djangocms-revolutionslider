# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('revolutionslider', '0006_auto_20150922_1152'),
    ]

    operations = [
        migrations.AddField(
            model_name='layer',
            name='h_offset',
            field=models.IntegerField(verbose_name='Horizontal offset', default=0, help_text='value in pixels'),
        ),
        migrations.AddField(
            model_name='layer',
            name='v_offset',
            field=models.IntegerField(verbose_name='Vertical offset', default=0, help_text='value in pixels'),
        ),
    ]
