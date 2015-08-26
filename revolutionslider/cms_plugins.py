from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from models import Slider


class SliderRevolution(CMSPluginBase):
    text_enabled = True
    allow_children = True
    render_template = "slider.html"
    model = Slider
    name = _("Revolution Slider")

    def render(self, context, instance, placeholder):
        context['instance'] = instance
        # print(dir(Slider.objects))

        context.update({
            'slides': instance.slide.all(),
            'url': reverse('admin:revolutionslider_slide_add')
        })
        return context

plugin_pool.register_plugin(SliderRevolution)