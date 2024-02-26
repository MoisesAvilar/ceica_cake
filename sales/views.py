from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from sales.models import Sale
from sales.serializers import SaleSerializer


class SalesCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer


class SalesRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
