from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _
from .models import Slider, Slide, Layer


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
    child_classes = ['Layer', ]
    model = Slide
    name = _("Slide")
    require_parent = True

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
            'placeholder': placeholder,
            })
        return context


class Layer(CMSPluginBase):
    module = _('Slider')
    render_template = "revolutionslider/layer.html"
    allow_children = True
    parent_class = ['Slide', ]
    model = Layer
    name = _("Layer")

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
            'placeholder': placeholder,
            })
        return context


plugin_pool.register_plugin(SliderRevolution)
plugin_pool.register_plugin(Slide)
plugin_pool.register_plugin(Layer)
