# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('revolutionslider', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slide',
            name='slider',
        ),
        migrations.AlterField(
            model_name='slide',
            name='easing',
            field=models.CharField(max_length=25, default=('OutBack', 'easeOutBack'), choices=[('OutBack', 'easeOutBack'), ('InQuad', 'easeInQuad'), ('OutQuad', 'easeOutQuad'), ('InOutQuad', 'easeInOutQuad'), ('InCubic', 'easeInCubic'), ('OutCubic', 'easeOutCubic'), ('InOutCubic', 'easeInOutCubic'), ('InQuart', 'easeInQuart'), ('OutQuart', 'easeOutQuart'), ('InOutQuart', 'easeInOutQuart'), ('InQuint', 'easeInQuint'), ('OutQuint', 'easeOutQuint'), ('InOutQuint', 'easeInOutQuint'), ('InSine', 'easeInSine'), ('OutSine', 'easeOutSine'), ('InOutSine', 'easeInOutSine'), ('InExpo', 'easeInExpo'), ('OutExpo', 'easeOutExpo'), ('InOutExpo', 'easeInOutExpo'), ('InCirc', 'easeInCirc'), ('OutCirc', 'easeOutCirc'), ('InOutCirc', 'easeInOutCirc'), ('InElastic', 'easeInElastic'), ('OutElastic', 'easeOutElastic'), ('InOutElastic', 'easeInOutElastic'), ('InBack', 'easeInBack'), ('OutBack', 'easeOutBack'), ('InOutBack', 'easeInOutBack'), ('InBounce', 'easeInBounce'), ('OutBounce', 'easeOutBounce'), ('InOutBounce', 'easeInOutBounce')]),
        ),
        migrations.AlterField(
            model_name='slide',
            name='image',
            field=models.ImageField(upload_to='revolution-slider/%Y/%m/%d', null=True, blank=True),
        ),
    ]
