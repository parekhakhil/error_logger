from rest_framework.response import Response
from django.conf import settings
from .models import Error
import traceback


class ErrorLogMiddleware:
    def __init__(self, get_response) -> None:
        self.get_response = get_response
        self.full_path = ""

    def __call__(self, request):
        response = self.get_response(request)
        full_path = request.build_absolute_uri()
        method = request.method
        if isinstance(response, Response):
            if response.status_code in settings.ERROR_STATUS:
                res_log = Error.objects.create(
                    request=str(full_path),
                    status_code=response.status_code,
                    error=traceback.format_exc(),
                    method=method,
                )
                response.status_code = 200
        return response

    # def process_view(self,request,view_func,view_args,view_kwargs):
    #     pass
    # def process_request(self):
    #     pass
    # def process_exception(self,request,exception):
    #     pass
    # def process_response(self):
    #     pass
