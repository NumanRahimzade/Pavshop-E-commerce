from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseForbidden


class BlockIPMiddleware(MiddlewareMixin):
    BLACKLIST = [
        '10.10.81.198',
    ]

    def process_view(self, request, *args, **kwargs):
        # if request.user.is_teacher
        print('isledi')
        if request.META['REMOTE_ADDR'] in self.BLACKLIST:
            return HttpResponseForbidden()