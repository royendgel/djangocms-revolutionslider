from django.db import models
from django.utils.translation import ugettext_lazy as _
from cms.models import CMSPlugin
from cms.utils.compat.dj import python_2_unicode_compatible


@python_2_unicode_compatible
class Slide(CMSPlugin):
    SLIDE_TRANSITION_CHOICES = (
        ('random-static', _('Random static')),
        ('slideup', 'Slide To Top'),
        ('slidedown', 'Slide To Bottom'),
        ('slideright', 'Slide To Right'),
        ('slideleft', 'Slide To Left'),
        ('slidehorizontal', 'Slide Horizontal (depending on Next/Previous)'),
        ('slidevertical', 'Slide Vertical (depending on Next/Previous)'),
        ('boxslide', 'Slide Boxes'),
        ('slotslide-horizontal', 'Slide Slots Horizontal'),
        ('slotslide-vertical', 'Slide Slots Vertical'),
        ('boxfade', 'Fade Boxes'),
        ('slotfade-horizontal', 'Fade Slots Horizontal'),
        ('slotfade-vertical', 'Fade Slots Vertical'),
        ('fadefromright', 'Fade and Slide from Right'),
        ('fadefromleft', 'Fade and Slide from Left'),
        ('fadefromtop', 'Fade and Slide from Top'),
        ('fadefrombottom', 'Fade and Slide from Bottom'),
        ('fadetoleftfadefromright', 'Fade To Left and Fade From Right'),
        ('fadetorightfadefromleft', 'Fade To Right and Fade From Left'),
        ('fadetotopfadefrombottom', 'Fade To Top and Fade From Bottom'),
        ('fadetobottomfadefromtop', 'Fade To Bottom and Fade From Top'),
        ('parallaxtoright', 'Parallax to Right'),
        ('parallaxtoleft', 'Parallax to Left'),
        ('parallaxtotop', 'Parallax to Top'),
        ('parallaxtobottom', 'Parallax to Bottom'),
        ('scaledownfromright', 'Zoom Out and Fade From Right'),
        ('scaledownfromleft', 'Zoom Out and Fade From Left'),
        ('scaledownfromtop', 'Zoom Out and Fade From Top'),
        ('scaledownfrombottom', 'Zoom Out and Fade From Bottom'),
        ('zoomout', 'ZoomOut'),
        ('zoomin', 'ZoomIn'),
        ('slotzoom-horizontal', 'Zoom Slots Horizontal'),
        ('slotzoom-vertical', 'Zoom Slots Vertical'),
        ('fade', 'Fade'),
        ('random', 'Random Flat and Premium'),
    )
    title = models.CharField(max_length=255, blank=True, null=True)
    master_speed = models.IntegerField(default=500, blank=False, null=True)
    image = models.ImageField(upload_to="revolution-slider/%Y/%m/%d", blank=True, null=True)
    transition = models.CharField(max_length=255, choices=SLIDE_TRANSITION_CHOICES, default=SLIDE_TRANSITION_CHOICES[0])

    def __str__(self):
        return u"{0}".format(self.title)


@python_2_unicode_compatible
class Layer(CMSPlugin):
    INCOMING_LAYER_ANIMATION = (
        ('', _("None")),
        ('sft', 'Short from Top'),
        ('sfb', 'Short from Bottom'),
        ('sfr', 'Short from Right'),
        ('sfl', 'Short from Left'),
        ('lft', 'Long from Top'),
        ('lfb', 'Long from Bottom'),
        ('lfr', 'Long from Right'),
        ('lfl', 'Long from Left'),
        ('skewfromleft', 'Skew from Left'),
        ('skewfromright', 'Skew from Right'),
        ('skewfromleftshort', 'Skew Short from Left'),
        ('skewfromrightshort', 'Skew Short from Right'),
        ('fade', 'fading'),
        ('randomrotate', 'Fade in, Rotate from a Random position and Degree')
    )
    OUTGOING_LAYER_ANIMATION = (
        ('', _("None")),
        ('stt', 'Short to Top'),
        ('stb', 'Short to Bottom'),
        ('str', 'Short to Right'),
        ('stl', 'Short to Left'),
        ('ltt', 'Long to Top'),
        ('ltb', 'Long to Bottom'),
        ('ltr', 'Long to Right'),
        ('ltl', 'Long to Left'),
        ('skewtoleft', 'Skew to Left'),
        ('skewtoright', 'Skew to Right'),
        ('skewtoleftshort', 'Skew Short to Left'),
        ('skewtorightshort', 'Skew Short to Right'),
        ('fadeout', 'fading'),
        ('randomrotateout', 'Fade in, Rotate from a Random position and Degree'),
    )
    SPLIT_CHOICES = (
        ('', _("Don't split")),
        ('chars', _('Characters')),
        ('words', _('Words')),
        ('lines', _('Lines')),
    )
    EASE_CHOICES = (
        ('OutBack', 'easeOutBack'),
        ('InQuad', 'easeInQuad'),
        ('OutQuad', 'easeOutQuad'),
        ('InOutQuad', 'easeInOutQuad'),
        ('InCubic', 'easeInCubic'),
        ('OutCubic', 'easeOutCubic'),
        ('InOutCubic', 'easeInOutCubic'),
        ('InQuart', 'easeInQuart'),
        ('OutQuart', 'easeOutQuart'),
        ('InOutQuart', 'easeInOutQuart'),
        ('InQuint', 'easeInQuint'),
        ('OutQuint', 'easeOutQuint'),
        ('InOutQuint', 'easeInOutQuint'),
        ('InSine', 'easeInSine'),
        ('OutSine', 'easeOutSine'),
        ('InOutSine', 'easeInOutSine'),
        ('InExpo', 'easeInExpo'),
        ('OutExpo', 'easeOutExpo'),
        ('InOutExpo', 'easeInOutExpo'),
        ('InCirc', 'easeInCirc'),
        ('OutCirc', 'easeOutCirc'),
        ('InOutCirc', 'easeInOutCirc'),
        ('InElastic', 'easeInElastic'),
        ('OutElastic', 'easeOutElastic'),
        ('InOutElastic', 'easeInOutElastic'),
        ('InBack', 'easeInBack'),
        ('OutBack', 'easeOutBack'),
        ('InOutBack', 'easeInOutBack'),
        ('InBounce', 'easeInBounce'),
        ('OutBounce', 'easeOutBounce'),
        ('InOutBounce', 'easeInOutBounce')
    )

    start = models.IntegerField(help_text='The timepoint in ms at which the layer should move in to the slide.', default=1000)
    end = models.IntegerField(help_text='The timepoint in ms at which the layer should move out from the slide.', default=2500, blank=True, null=True)
    speed = models.IntegerField(
        help_text='The speed in ms of the transition to move the layer in the slide at the defined timepoint.',
        default=100, blank=True,
        null=True
    )
    position_x = models.CharField(
        help_text=_("Possible values are 'left', 'center', 'right', or any Value between -2500  and 2500."),
        max_length=255,
        default="center",
    )
    position_y = models.CharField(
        help_text="Possible Values are 'top', 'center', 'bottom', or any Value between -2500 and 2500.",
        max_length=255,
        default="center",
    )
    v_offset = models.IntegerField(_("Vertical offset"), help_text="value in pixels", default=0)
    h_offset = models.IntegerField(_("Horizontal offset"), help_text="value in pixels", default=0)
    incoming_animation = models.CharField(max_length=255, choices=INCOMING_LAYER_ANIMATION, default=INCOMING_LAYER_ANIMATION[0], blank=True)
    outgoing_animation = models.CharField(max_length=255, choices=OUTGOING_LAYER_ANIMATION, default=OUTGOING_LAYER_ANIMATION[0], blank=True)
    easing = models.CharField(max_length=25, choices=EASE_CHOICES, default=EASE_CHOICES[0])
    layer_text = models.TextField(max_length=255, blank=True)
    splitin = models.CharField(max_length=255, choices=SPLIT_CHOICES, default=SPLIT_CHOICES[0], blank=True)
    splitout = models.CharField(max_length=255, choices=SPLIT_CHOICES, default=SPLIT_CHOICES[0], blank=True)
    elementdelay = models.FloatField(
        help_text="A Value between 0 and 1 to make delays between the 'splitted text element' start animation.",
        default=0,
        blank=True,
        null=True
    )
    endelementdelay = models.FloatField(
        help_text="A Value between 0 and 1 to make delays between the 'splitted text element' end animation.",
        default=0,
        blank=True,
        null=True
    )
    style = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return u"{0}".format(self.layer_text)


@python_2_unicode_compatible
class Slider(CMSPlugin):
    master_start = models.IntegerField(default=1000, blank=True)
    master_end = models.IntegerField(default=5000, blank=False, null=True)

    def __str__(self):
        return "Revolution Slider"
