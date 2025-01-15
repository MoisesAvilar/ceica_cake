from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from cashflow.models import Cashflow
from cashflow.serializers import CashflowSerializer


class CashflowCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Cashflow.objects.all()
    serializer_class = CashflowSerializer


class CashflowRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Cashflow.objects.all()
    serializer_class = CashflowSerializer
