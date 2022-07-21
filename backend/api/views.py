import json
#from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.models import Product
from django.forms.models import model_to_dict
from products.serializers import ProductSerializer


# @api_view(["GET"])
# def api_home(request, *args, **kwargs):
#   instance = Product.objects.all().order_by("?").first()
# data = {}
#  if instance:
#  data = model_to_dict(instance, fields=['id', 'title', 'price'])
#  data['title'] = model_data.title
#  data['content'] = model_data.content
#  data['price'] = model_data.price
#    data = ProductSerializer(instance).data
# return Response(data)


@api_view(["POST"])
def api_home(request, *args, **kwargs):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # print(serializer.data)
        return Response(serializer.data)
    return Response({"invalid": "not good"}, status=400)
