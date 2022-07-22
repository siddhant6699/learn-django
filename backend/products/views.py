import imp
from itertools import product
from django.shortcuts import get_object_or_404
from requests import Response
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer

# CAN BE USE TO CREATE NEW PRODUCT
# class ProductCreateAPIView(generics.CreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

#     # def perform_create(self, serializer):
#     #     title = serializer.validated_data.get("title")
#     #     content = serializer.validated_data.get("content")
#     #     or None
#     #     if content is None:
#     #         content = title
#     #     serializer.save(content=content)

# product_create_view = ProductCreateAPIView.as_view()


# CAN BE USE TO GET ALL PRODUCTS AND CREATE NEW ONE AT THE SAME TIME
class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # def perform_create(self, serializer):
    #     title = serializer.validated_data.get("title")
    #     content = serializer.validated_data.get("content")
    #     or None
    #     if content is None:
    #         content = title
    #     serializer.save(content=content)


product_list_create_view = ProductListCreateAPIView.as_view()


# USED TO GET DETAILED VIEW OF A PRODUCT
class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


product_detail_view = ProductDetailAPIView.as_view()


class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    # WE CAN DEFINE METHOD TO PERFORM HERE
    # def perofrm_update(self,serializer):


product_update_view = ProductUpdateAPIView.as_view()


class ProductDestroyAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        return super().perform_destroy(instance)

product_destroy_view = ProductDestroyAPIView.as_view()


# USE THIS SINGLE FUNCTION FOR ALL GET AND POST
# @api_view(['GET', 'POST'])
# def product_alt_view(request, pk=None, *args, **kwargs):
#     method = request.method

#     if method == "GET":
#         if pk is not None:
#             # detail view
#             obj = get_object_or_404(Product, pk=pk)
#             data = ProductSerializer(obj, many=False).data
#             return Response(data)
#         # list view
#         queryset = Product.objects.all()
#         data = ProductSerializer(queryset, many=True).data
#         print(data)
#         return Response(data)

#     if method == "POST":
#         serializer = ProductSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             return Response(serializer.data)
