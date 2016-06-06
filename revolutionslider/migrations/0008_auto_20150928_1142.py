# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('revolutionslider', '0007_auto_20150923_1738'),
    ]

    operations = [
        migrations.AddField(
            model_name='layer',
            name='style',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='layer',
            name='incoming_animation',
            field=models.CharField(choices=[('', 'None'), ('sft', 'Short from Top'), ('sfb', 'Short from Bottom'), ('sfr', 'Short from Right'), ('sfl', 'Short from Left'), ('lft', 'Long from Top'), ('lfb', 'Long from Bottom'), ('lfr', 'Long from Right'), ('lfl', 'Long from Left'), ('skewfromleft', 'Skew from Left'), ('skewfromright', 'Skew from Right'), ('skewfromleftshort', 'Skew Short from Left'), ('skewfromrightshort', 'Skew Short from Right'), ('fade', 'fading'), ('randomrotate', 'Fade in, Rotate from a Random position and Degree')], blank=True, max_length=255, default=('', 'None')),
        ),
        migrations.AlterField(
            model_name='layer',
            name='outgoing_animation',
            field=models.CharField(choices=[('', 'None'), ('stt', 'Short to Top'), ('stb', 'Short to Bottom'), ('str', 'Short to Right'), ('stl', 'Short to Left'), ('ltt', 'Long to Top'), ('ltb', 'Long to Bottom'), ('ltr', 'Long to Right'), ('ltl', 'Long to Left'), ('skewtoleft', 'Skew to Left'), ('skewtoright', 'Skew to Right'), ('skewtoleftshort', 'Skew Short to Left'), ('skewtorightshort', 'Skew Short to Right'), ('fadeout', 'fading'), ('randomrotateout', 'Fade in, Rotate from a Random position and Degree')], blank=True, max_length=255, default=('', 'None')),
        ),
    ]
