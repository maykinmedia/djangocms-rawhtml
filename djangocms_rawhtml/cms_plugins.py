from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext as _
from djangocms_rawhtml.models import (
    RawHTMLPluginData, TwoColumnRawHTMLPluginData, ThreeColumnRawHTMLPluginData,
    FourColumnRawHTMLPluginData
)


@plugin_pool.register_plugin
class RawHTMLPluginPublisher(CMSPluginBase):
    """
    Plugin to manage ran HTML text that needs to be managed from the admin interface.
    """
    name = _("Raw HTML")
    model = RawHTMLPluginData
    change_form_template = "admin/djangocms_rawhtml/change_form.html"
    render_template = "djangocms_rawhtml/plugins/raw.html"
    allow_children = False

    def render(self, context, instance, placeholder):
        context.update({ 'instance': instance })
        return context


@plugin_pool.register_plugin
class TwoColumnRawHTMLPluginPublisher(CMSPluginBase):
    """
    Plugin to manage ran HTML text that needs to be managed from the admin interface.
    """
    name = _("2 Column Raw HTML")
    model = TwoColumnRawHTMLPluginData
    change_form_template = "admin/djangocms_rawhtml/change_form.html"
    render_template = "djangocms_rawhtml/plugins/two_column_raw.html"
    allow_children = False

    def render(self, context, instance, placeholder):
        context.update({ 'instance': instance })
        return context


@plugin_pool.register_plugin
class ThreeColumnRawHTMLPluginPublisher(CMSPluginBase):
    """
    Plugin to manage ran HTML text that needs to be managed from the admin interface.
    """
    name = _("3 Column Raw HTML")
    model = ThreeColumnRawHTMLPluginData
    change_form_template = "admin/djangocms_rawhtml/change_form.html"
    render_template = "djangocms_rawhtml/plugins/three_column_raw.html"
    allow_children = False

    def render(self, context, instance, placeholder):
        context.update({ 'instance': instance })
        return context


@plugin_pool.register_plugin
class FourColumnRawHTMLPluginPublisher(CMSPluginBase):
    """
    Plugin to manage ran HTML text that needs to be managed from the admin interface.
    """
    name = _("4 Column Raw HTML")
    model = FourColumnRawHTMLPluginData
    change_form_template = "admin/djangocms_rawhtml/change_form.html"
    render_template = "djangocms_rawhtml/plugins/four_column_raw.html"
    allow_children = False

    def render(self, context, instance, placeholder):
        context.update({ 'instance': instance })
        return context
