from django_shopping_cart.server_config import PROJECT_NAME

def constants(request):
    return {'PROJECT_NAME': PROJECT_NAME}
