from django_shopping_cart import server_config


def constants(request):
    return {'PROJECT_NAME': server_config.PROJECT_NAME,
            'FRONTEND_SERVER_LOCATION': server_config.FRONTEND_SERVER_LOCATION}
