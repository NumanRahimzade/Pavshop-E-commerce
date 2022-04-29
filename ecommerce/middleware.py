from urllib import response
from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseForbidden


class BlockIPMiddleware(MiddlewareMixin):
    BLACKLIST = [
        '',# ip has to be inserted here
    ]

    def process_view(self, request, *args, **kwargs):
        # if request.user.is_teacher
        print('isledi')
        if request.META['REMOTE_ADDR'] in self.BLACKLIST:
            return HttpResponseForbidden()


class LogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response


    def __call__(self, request):
        response = self.get_response(request)

        return response

