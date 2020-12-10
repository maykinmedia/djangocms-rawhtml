from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from cms.models.pluginmodel import CMSPlugin
from django.utils.text import Truncator
from django.utils.html import strip_tags


@python_2_unicode_compatible
class RawHTMLPluginData(CMSPlugin):
    """
    Model for Raw HTML Plugin

    body - contains the HTML source text
    label - used for display purposes on the admin site
    """

    label = models.CharField(max_length=40, default="")
    body = models.TextField('HTML')
    full_width = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return Truncator(strip_tags(self.label).replace('&shy;', '')).words(5, truncate="...")

    def __unicode__(self):
        return Truncator(strip_tags(self.label).replace('&shy;', '')).words(5, truncate="...")


@python_2_unicode_compatible
class TwoColumnRawHTMLPluginData(CMSPlugin):
    """
    Model for Raw HTML Plugin

    body - contains the HTML source text
    label - used for display purposes on the admin site
    """

    label = models.CharField(max_length=40, default="")
    body_left = models.TextField('HTML left')
    body_right = models.TextField('HTML right')
    full_width = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return Truncator(strip_tags(self.label).replace('&shy;', '')).words(5, truncate="...")

    def __unicode__(self):
        return Truncator(strip_tags(self.label).replace('&shy;', '')).words(5, truncate="...")


@python_2_unicode_compatible
class ThreeColumnRawHTMLPluginData(CMSPlugin):
    """
    Model for Raw HTML Plugin

    body - contains the HTML source text
    label - used for display purposes on the admin site
    """

    label = models.CharField(max_length=40, default="")
    body_left = models.TextField('HTML left')
    body_middle = models.TextField('HTML middle')
    body_right = models.TextField('HTML right')
    full_width = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return Truncator(strip_tags(self.label).replace('&shy;', '')).words(5, truncate="...")

    def __unicode__(self):
        return Truncator(strip_tags(self.label).replace('&shy;', '')).words(5, truncate="...")


@python_2_unicode_compatible
class FourColumnRawHTMLPluginData(CMSPlugin):
    """
    Model for Raw HTML Plugin

    body - contains the HTML source text
    label - used for display purposes on the admin site
    """

    label = models.CharField(max_length=40, default="")
    body_left = models.TextField('HTML left')
    body_middle_left = models.TextField('HTML middle left')
    body_middle_right = models.TextField('HTML middle right')
    body_right = models.TextField('HTML right')
    full_width = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return Truncator(strip_tags(self.label).replace('&shy;', '')).words(5, truncate="...")

    def __unicode__(self):
        return Truncator(strip_tags(self.label).replace('&shy;', '')).words(5, truncate="...")
