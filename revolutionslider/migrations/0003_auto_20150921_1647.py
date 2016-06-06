# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0012_auto_20150607_2207'),
        ('revolutionslider', '0002_auto_20150918_1631'),
    ]

    operations = [
        migrations.CreateModel(
            name='Layer',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, parent_link=True, to='cms.CMSPlugin', serialize=False, primary_key=True)),
                ('start', models.IntegerField(help_text='Point in time (ms) this layer starts', default=1000)),
                ('end', models.IntegerField(default=2500, blank=True, null=True)),
                ('speed', models.IntegerField(default=100, blank=True, null=True)),
                ('position_x', models.CharField(help_text="value in pixels or 'center'", max_length=255, default='center', null=True)),
                ('position_y', models.CharField(help_text="value in pixels or 'top', 'bottom'", max_length=255, default=70, null=True)),
                ('easing', models.CharField(max_length=25, choices=[('OutBack', 'easeOutBack'), ('InQuad', 'easeInQuad'), ('OutQuad', 'easeOutQuad'), ('InOutQuad', 'easeInOutQuad'), ('InCubic', 'easeInCubic'), ('OutCubic', 'easeOutCubic'), ('InOutCubic', 'easeInOutCubic'), ('InQuart', 'easeInQuart'), ('OutQuart', 'easeOutQuart'), ('InOutQuart', 'easeInOutQuart'), ('InQuint', 'easeInQuint'), ('OutQuint', 'easeOutQuint'), ('InOutQuint', 'easeInOutQuint'), ('InSine', 'easeInSine'), ('OutSine', 'easeOutSine'), ('InOutSine', 'easeInOutSine'), ('InExpo', 'easeInExpo'), ('OutExpo', 'easeOutExpo'), ('InOutExpo', 'easeInOutExpo'), ('InCirc', 'easeInCirc'), ('OutCirc', 'easeOutCirc'), ('InOutCirc', 'easeInOutCirc'), ('InElastic', 'easeInElastic'), ('OutElastic', 'easeOutElastic'), ('InOutElastic', 'easeInOutElastic'), ('InBack', 'easeInBack'), ('OutBack', 'easeOutBack'), ('InOutBack', 'easeInOutBack'), ('InBounce', 'easeInBounce'), ('OutBounce', 'easeOutBounce'), ('InOutBounce', 'easeInOutBounce')], default=('OutBack', 'easeOutBack'))),
                ('layer_text', models.TextField(max_length=255, blank=True)),
                ('splitin', models.CharField(max_length=255, choices=[('chars', 'Characters')], default=('chars', 'Characters'))),
                ('splitout', models.CharField(max_length=255, choices=[('chars', 'Characters')], default=('chars', 'Characters'))),
                ('elementdelay', models.IntegerField(default=0.1, blank=True, null=True)),
                ('endelementdelay', models.IntegerField(default=0.1, blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.RemoveField(
            model_name='slide',
            name='easing',
        ),
        migrations.RemoveField(
            model_name='slide',
            name='end',
        ),
        migrations.RemoveField(
            model_name='slide',
            name='position_x',
        ),
        migrations.RemoveField(
            model_name='slide',
            name='position_y',
        ),
        migrations.RemoveField(
            model_name='slide',
            name='slide_text',
        ),
        migrations.RemoveField(
            model_name='slide',
            name='speed',
        ),
        migrations.RemoveField(
            model_name='slide',
            name='start',
        ),
        migrations.RemoveField(
            model_name='slider',
            name='master_speed',
        ),
        migrations.AddField(
            model_name='slide',
            name='master_speed',
            field=models.IntegerField(default=500, null=True),
        ),
        migrations.AddField(
            model_name='slide',
            name='title',
            field=models.CharField(max_length=255, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='slide',
            name='transition',
            field=models.CharField(max_length=255, choices=[('random-static', 'Random static')], default=('random-static', 'Random static')),
        ),
    ]
