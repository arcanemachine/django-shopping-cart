from django.http import HttpResponseRedirect  # , JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
# from django.views.decorators.clickjacking import xframe_options_exempt

from django_shopping_cart import server_config

FRONTEND_SERVER_LOCATION = server_config.FRONTEND_SERVER_LOCATION
FRONTEND_LOGIN_URL = server_config.FRONTEND_LOGIN_URL


def project_root(request):
    return render(request, 'project_root.html')


# def hello_cookie(request):
#     response = \
#         HttpResponseRedirect(FRONTEND_SERVER_LOCATION + FRONTEND_LOGIN_URL)
#     response.set_cookie(key="hello", value=123, httponly=True)
#     return response


# @ensure_csrf_cookie
# def get_csrftoken(request):
#     response = \
#         HttpResponseRedirect(FRONTEND_SERVER_LOCATION + FRONTEND_LOGIN_URL)
#     response.set_cookie(key="hello", value=123)
#     return response
