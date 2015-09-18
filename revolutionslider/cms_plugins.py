from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _
from .models import Slider, Slide


class SliderRevolution(CMSPluginBase):
    module = _('Slider')
    text_enabled = True
    allow_children = True
    render_template = "revolutionslider/slider.html"
    model = Slider
    name = _("Revolution Slider")
    child_classes = ['Slide', ]

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
            'placeholder': placeholder,
        })
        return context


class Slide(CMSPluginBase):
    module = _('Slider')
    render_template = "revolutionslider/slide.html"
    allow_children = True
    parent_class = ['SliderRevolution', ]
    model = Slide
    name = _("Slide")

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
            'placeholder': placeholder,
            })
        return context

plugin_pool.register_plugin(SliderRevolution)
plugin_pool.register_plugin(Slide)
