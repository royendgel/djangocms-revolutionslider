# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('revolutionslider', '0003_auto_20150921_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='layer',
            name='elementdelay',
            field=models.FloatField(default=0.1, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='layer',
            name='endelementdelay',
            field=models.FloatField(default=0.1, blank=True, null=True),
        ),
    ]
