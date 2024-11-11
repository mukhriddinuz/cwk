from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin


class Redirect404Middleware(MiddlewareMixin):
    def process_response(self, request, response):
        if response.status_code == 404:
            return redirect('https://cwkedu.uz')  # yo'naltiriladigan sahifa URL
        return response