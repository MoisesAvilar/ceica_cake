from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from customers.models import Customer
from customers.serializers import CustomerSerializer
from app.pagination import StandardResultsSetPagination


class CustomerCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    pagination_class = StandardResultsSetPagination


class CustomerRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
