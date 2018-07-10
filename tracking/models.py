from django.utils import timezone

import logging
from django.db import models

log = logging.getLogger('tracking.models')

class Visitors(models.Model):
    session_key = models.CharField(max_length=40)
    ip_address = models.CharField(max_length=20)
    user_agent = models.CharField(max_length=255)
    referrer = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    request_method = models.CharField(max_length=5)
    aff_id = models.CharField(max_length=20, null=True, blank=True)
    language = models.CharField(max_length=5, null=True, blank=True)
    is_bot = models.BooleanField(default=False)
    created_at = models.DateTimeField()

    def __init__(self, *args, **kwargs):
        super(Visitors, self).__init__(*args, **kwargs)
        self.created_at = timezone.now()

    class Meta:
        verbose_name = 'Visitor'
        verbose_name_plural = 'Visitors'

class UntrackedUserAgent(models.Model):
    keyword = models.CharField('keyword', max_length=100, help_text=
        'Part or all of a user-agent string.  For example, "Googlebot" here will be found in "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)" and that visitor will not be tracked.')

    def __unicode__(self):
        return self.keyword

    class Meta:
        ordering = ('keyword',)
        verbose_name = 'Untracked User-Agent'
        verbose_name_plural = 'Untracked User-Agents'

class BannedIP(models.Model):
    ip_address = models.GenericIPAddressField('IP Address', help_text='The IP address that should be banned')

    def __unicode__(self):
        return self.ip_address

    class Meta:
        ordering = ['ip_address']
        verbose_name = 'Banned IP'
        verbose_name_plural = 'Banned IPs'