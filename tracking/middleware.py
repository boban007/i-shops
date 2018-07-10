import logging

from django.db.utils import DatabaseError
from django.utils.translation import get_language

from tracking import utils
from .models import Visitors

log = logging.getLogger('tracking.middleware')

class VisitorsTrackingMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response
    # One-time configuration and initialization.

#     @property
#     def proxies(self):
#         """Returns a list of URL prefixes that we should not track"""
#
#         if not hasattr(self, ('_prefixes')):
#             self._prefixes = getattr(settings, 'NO_TRACKING_PREFIXES', [])
#
#             if not getattr(settings,'_FREEZY_TRACKING_PREFIXES', False):
#                 for name in ('MEDIA_URL', 'STATIC_URL'):
#                     url = getattr(settings, name)
#                     if url and url != '/':
#                         self._prefixes.append(url)
#
#                 try:
#                     self._prefixes.append(reverse('tracking-refresh-active-users'))
#                 except NoReverseMatch:
#                     pass
#
#         return self._prefixes

    def __call__(self, request):

        # Code to be executed for each request before
        # the view (and later middleware) are called.

        aff_id = request.GET.get('aff_id', default=None)
        if aff_id:
            aff_id = aff_id[:20]

        attrs = {
            'session_key': request.session.session_key,
            'ip_address': utils.get_ip(request),
            'user_agent': request.META.get('HTTP_USER_AGENT', '')[:255],
            'referrer': request.META.get('HTTP_REFERER', 'unknown')[:255],
            'url': request.path,
            'request_method': request.method,
            'aff_id': aff_id,
            'language': get_language(),
            'is_bot': False,
        }

        try:
             Visitors.objects.create(**attrs)
        except DatabaseError:
            log.error('There was a problem saving visitor information:\n%s', locals())

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

# class BannedIPMiddleware:
#
#     def process_request(self, request):
#         key = '_tracking_banned_ips'
#         ips = cache.get(key)
#         if ips is None:
#             log.info('Updating banned IPs cache')
#             ips = [b.ip_address for b in BannedIP.objects.all()]
#             cache.set(key, ips, 3600)
#         if utils.get_ip(request) in ips:
#             raise Http404