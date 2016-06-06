# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('revolutionslider', '0004_auto_20150921_2055'),
    ]

    operations = [
        migrations.AddField(
            model_name='layer',
            name='incoming_animation',
            field=models.CharField(default=('sft', 'Short from Top'), max_length=255, choices=[('sft', 'Short from Top'), ('sfb', 'Short from Bottom'), ('sfr', 'Short from Right'), ('sfl', 'Short from Left'), ('lft', 'Long from Top'), ('lfb', 'Long from Bottom'), ('lfr', 'Long from Right'), ('lfl', 'Long from Left'), ('skewfromleft', 'Skew from Left'), ('skewfromright', 'Skew from Right'), ('skewfromleftshort', 'Skew Short from Left'), ('skewfromrightshort', 'Skew Short from Right'), ('fade', 'fading'), ('randomrotate', 'Fade in, Rotate from a Random position and Degree')]),
        ),
        migrations.AddField(
            model_name='layer',
            name='outgoing_animation',
            field=models.CharField(default=('stt', 'Short to Top'), max_length=255, choices=[('stt', 'Short to Top'), ('stb', 'Short to Bottom'), ('str', 'Short to Right'), ('stl', 'Short to Left'), ('ltt', 'Long to Top'), ('ltb', 'Long to Bottom'), ('ltr', 'Long to Right'), ('ltl', 'Long to Left'), ('skewtoleft', 'Skew to Left'), ('skewtoright', 'Skew to Right'), ('skewtoleftshort', 'Skew Short to Left'), ('skewtorightshort', 'Skew Short to Right'), ('fadeout', 'fading'), ('randomrotateout', 'Fade in, Rotate from a Random position and Degree')]),
        ),
        migrations.AlterField(
            model_name='layer',
            name='elementdelay',
            field=models.FloatField(blank=True, null=True, help_text="A Value between 0 and 1 to make delays between the 'splitted text element' start animation.", default=0),
        ),
        migrations.AlterField(
            model_name='layer',
            name='end',
            field=models.IntegerField(blank=True, null=True, help_text='The timepoint in ms at which the layer should move out from the slide.', default=2500),
        ),
        migrations.AlterField(
            model_name='layer',
            name='endelementdelay',
            field=models.FloatField(blank=True, null=True, help_text="A Value between 0 and 1 to make delays between the 'splitted text element' end animation.", default=0),
        ),
        migrations.AlterField(
            model_name='layer',
            name='position_x',
            field=models.CharField(default='center', max_length=255, help_text="Possible values are 'left', 'center', 'right', or any Value between -2500  and 2500."),
        ),
        migrations.AlterField(
            model_name='layer',
            name='position_y',
            field=models.CharField(default='center', max_length=255, help_text="Possible Values are 'top', 'center', 'bottom', or any Value between -2500 and 2500."),
        ),
        migrations.AlterField(
            model_name='layer',
            name='speed',
            field=models.IntegerField(blank=True, null=True, help_text='The speed in ms of the transition to move the layer in the slide at the defined timepoint.', default=100),
        ),
        migrations.AlterField(
            model_name='layer',
            name='splitin',
            field=models.CharField(default=('', "Don't split"), max_length=255, choices=[('', "Don't split"), ('chars', 'Characters'), ('words', 'Words'), ('lines', 'Lines')]),
        ),
        migrations.AlterField(
            model_name='layer',
            name='splitout',
            field=models.CharField(default=('', "Don't split"), max_length=255, choices=[('', "Don't split"), ('chars', 'Characters'), ('words', 'Words'), ('lines', 'Lines')]),
        ),
        migrations.AlterField(
            model_name='layer',
            name='start',
            field=models.IntegerField(default=1000, help_text='The timepoint in ms at which the layer should move in to the slide.'),
        ),
        migrations.AlterField(
            model_name='slide',
            name='transition',
            field=models.CharField(default=('random-static', 'Random static'), max_length=255, choices=[('random-static', 'Random static'), ('slideup', 'Slide To Top'), ('slidedown', 'Slide To Bottom'), ('slideright', 'Slide To Right'), ('slideleft', 'Slide To Left'), ('slidehorizontal', 'Slide Horizontal (depending on Next/Previous)'), ('slidevertical', 'Slide Vertical (depending on Next/Previous)'), ('boxslide', 'Slide Boxes'), ('slotslide-horizontal', 'Slide Slots Horizontal'), ('slotslide-vertical', 'Slide Slots Vertical'), ('boxfade', 'Fade Boxes'), ('slotfade-horizontal', 'Fade Slots Horizontal'), ('slotfade-vertical', 'Fade Slots Vertical'), ('fadefromright', 'Fade and Slide from Right'), ('fadefromleft', 'Fade and Slide from Left'), ('fadefromtop', 'Fade and Slide from Top'), ('fadefrombottom', 'Fade and Slide from Bottom'), ('fadetoleftfadefromright', 'Fade To Left and Fade From Right'), ('fadetorightfadefromleft', 'Fade To Right and Fade From Left'), ('fadetotopfadefrombottom', 'Fade To Top and Fade From Bottom'), ('fadetobottomfadefromtop', 'Fade To Bottom and Fade From Top'), ('parallaxtoright', 'Parallax to Right'), ('parallaxtoleft', 'Parallax to Left'), ('parallaxtotop', 'Parallax to Top'), ('parallaxtobottom', 'Parallax to Bottom'), ('scaledownfromright', 'Zoom Out and Fade From Right'), ('scaledownfromleft', 'Zoom Out and Fade From Left'), ('scaledownfromtop', 'Zoom Out and Fade From Top'), ('scaledownfrombottom', 'Zoom Out and Fade From Bottom'), ('zoomout', 'ZoomOut'), ('zoomin', 'ZoomIn'), ('slotzoom-horizontal', 'Zoom Slots Horizontal'), ('slotzoom-vertical', 'Zoom Slots Vertical'), ('fade', 'Fade'), ('random', 'Random Flat and Premium')]),
        ),
    ]
