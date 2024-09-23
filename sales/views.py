from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse

from sales.models import Sale
from sales.serializers import SaleSerializer
from sales.product_list import PRODUCT

class SalesCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer


class SalesRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer


class ProductListView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get(self, request):
        products = [{'value': key, 'label': value} for key, value in PRODUCT]
        return JsonResponse(products, safe=False)