from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from customers.models import Customer
from customers.serializers import CustomerSerializer
from app.pagination import StandardResultsSetPagination
from rest_framework.filters import SearchFilter


class CustomerCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [SearchFilter]
    search_fields = ['name']


class CustomerRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerAllListView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Customer.objects.all().order_by('name')
    serializer_class = CustomerSerializer
    pagination_class = None
