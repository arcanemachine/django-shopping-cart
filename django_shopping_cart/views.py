from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie

from django_shopping_cart import server_config


def project_root(request):
    return render(request, 'project_root.html')

@ensure_csrf_cookie
def get_csrftoken(request):
    frontend_server_location = server_config.FRONTEND_SERVER_LOCATION
    frontend_login_url = server_config.FRONTEND_LOGIN_URL
    return HttpResponseRedirect(frontend_server_location + frontend_login_url)
