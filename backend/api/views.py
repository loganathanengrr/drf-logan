from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.models import Product
from products.serializers import ProductSerializer

@api_view(["GET"])
def api_home(request, *args, **kwargs):
    """
    DRF api view
    """
    instance = Product.objects.all().order_by("?").first() # returns random model instance.
    data = {}
    if instance:
        data = ProductSerializer(instance).data

    return Response(data)
