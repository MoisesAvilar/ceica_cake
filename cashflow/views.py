from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated
from cashflow.models import Cashflow
from cashflow.serializers import CashflowSerializer
from app.pagination import StandardResultsSetPagination


class CashflowCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CashflowSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['date']
    ordering = ['-date']

    def get_queryset(self):
        """
        Filtra os registros de fluxo de caixa por um intervalo de datas,
        se os parâmetros start_date e end_date forem fornecidos.
        """
        queryset = Cashflow.objects.all()
        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')

        if start_date and end_date:
            queryset = queryset.filter(date__range=[start_date, end_date])
        
        return queryset


class CashflowRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Cashflow.objects.all()
    serializer_class = CashflowSerializer
