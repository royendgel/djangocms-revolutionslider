# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_auto_20140926_2347'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('image', models.ImageField(null=True, upload_to=b'', blank=True)),
                ('slide_text', models.CharField(max_length=2500, null=True, blank=True)),
                ('start', models.IntegerField(default=1000, null=True, blank=True)),
                ('end', models.IntegerField(default=5000, null=True)),
                ('speed', models.IntegerField(default=100, null=True)),
                ('position_x', models.IntegerField(default=477, null=True)),
                ('position_y', models.IntegerField(default=180, null=True)),
                ('easing', models.CharField(default=(b'OutBack', b'easeOutBack'), max_length=25, choices=[(b'OutBack', b'easeOutBack'), (b'InQuad', b'easeInQuad'), (b'OutQuad', b'easeOutQuad'), (b'InOutQuad', b'easeInOutQuad'), (b'InCubic', b'easeInCubic'), (b'OutCubic', b'easeOutCubic'), (b'InOutCubic', b'easeInOutCubic'), (b'InQuart', b'easeInQuart'), (b'OutQuart', b'easeOutQuart'), (b'InOutQuart', b'easeInOutQuart'), (b'InQuint', b'easeInQuint'), (b'OutQuint', b'easeOutQuint'), (b'InOutQuint', b'easeInOutQuint'), (b'InSine', b'easeInSine'), (b'OutSine', b'easeOutSine'), (b'InOutSine', b'easeInOutSine'), (b'InExpo', b'easeInExpo'), (b'OutExpo', b'easeOutExpo'), (b'InOutExpo', b'easeInOutExpo'), (b'InCirc', b'easeInCirc'), (b'OutCirc', b'easeOutCirc'), (b'InOutCirc', b'easeInOutCirc'), (b'InElastic', b'easeInElastic'), (b'OutElastic', b'easeOutElastic'), (b'InOutElastic', b'easeInOutElastic'), (b'InBack', b'easeInBack'), (b'OutBack', b'easeOutBack'), (b'InOutBack', b'easeInOutBack'), (b'InBounce', b'easeInBounce'), (b'OutBounce', b'easeOutBounce'), (b'InOutBounce', b'easeInOutBounce')])),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('master_start', models.IntegerField(default=1000, blank=True)),
                ('master_end', models.IntegerField(default=5000, null=True)),
                ('master_speed', models.IntegerField(default=300, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.AddField(
            model_name='slide',
            name='slider',
            field=models.ForeignKey(related_name='slide', blank=True, to='revolutionslider.Slider', null=True),
            preserve_default=True,
        ),
    ]
