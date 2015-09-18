from django.db import models
from django.utils.translation import ugettext_lazy as _
from cms.models import CMSPlugin


EASE_CHOICES = (
    ('OutBack', 'easeOutBack'), ('InQuad', 'easeInQuad'), ('OutQuad', 'easeOutQuad'), ('InOutQuad', 'easeInOutQuad'),
    ('InCubic', 'easeInCubic'), ('OutCubic', 'easeOutCubic'), ('InOutCubic', 'easeInOutCubic'),
    ('InQuart', 'easeInQuart'),
    ('OutQuart', 'easeOutQuart'), ('InOutQuart', 'easeInOutQuart'), ('InQuint', 'easeInQuint'),
    ('OutQuint', 'easeOutQuint'), ('InOutQuint', 'easeInOutQuint'), ('InSine', 'easeInSine'),
    ('OutSine', 'easeOutSine'),
    ('InOutSine', 'easeInOutSine'), ('InExpo', 'easeInExpo'), ('OutExpo', 'easeOutExpo'),
    ('InOutExpo', 'easeInOutExpo'),
    ('InCirc', 'easeInCirc'), ('OutCirc', 'easeOutCirc'), ('InOutCirc', 'easeInOutCirc'),
    ('InElastic', 'easeInElastic'),
    ('OutElastic', 'easeOutElastic'), ('InOutElastic', 'easeInOutElastic'), ('InBack', 'easeInBack'),
    ('OutBack', 'easeOutBack'), ('InOutBack', 'easeInOutBack'), ('InBounce', 'easeInBounce'),
    ('OutBounce', 'easeOutBounce'), ('InOutBounce', 'easeInOutBounce')
)


class Slide(CMSPlugin):
    image = models.ImageField(upload_to="revolution-slider/%Y/%m/%d", blank=True, null=True)
    slide_text = models.CharField(max_length=2500, blank=True, null=True)
    start = models.IntegerField(default=1000, blank=True, null=True)
    end = models.IntegerField(default=5000, blank=False, null=True)
    speed = models.IntegerField(default=100, blank=False, null=True)
    position_x = models.IntegerField(default=477, blank=False, null=True)
    position_y = models.IntegerField(default=180, blank=False, null=True)
    easing = models.CharField(max_length=25, choices=EASE_CHOICES, default=EASE_CHOICES[0])

    def __unicode__(self):
        return "%s" % (self.id)


class Slider(CMSPlugin):
    master_start = models.IntegerField(default=1000, blank=True)
    master_end = models.IntegerField(default=5000, blank=False, null=True)
    master_speed = models.IntegerField(default=300, blank=False, null=True)

    def __unicode__(self):
        return _(u"Revolution Slider")
