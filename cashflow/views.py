from datetime import datetime
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
    ordering_fields = ["date"]
    ordering = ["-date"]

    def get_queryset(self):
        """
        Filtra os registros de fluxo de caixa por um intervalo de datas,
        se os parâmetros start_date e end_date forem fornecidos.
        """
        queryset = Cashflow.objects.all()
        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')

        print(f"--- DEBUG CASHFLOW ---")
        print(f"Params recebidos: start={start_date}, end={end_date}")

        if start_date and end_date:
            try:
                # Forçamos a conversão para garantir que não são strings vazias ou nulas
                start = datetime.strptime(start_date, '%Y-%m-%d').date()
                end = datetime.strptime(end_date, '%Y-%m-%d').date()
                
                queryset = queryset.filter(date__gte=start, date__lte=end)
                
                print(f"SQL gerado: {queryset.query}")
                print(f"Resultados encontrados: {queryset.count()}")
            except Exception as e:
                print(f"Erro no filtro: {e}")
        
        print(f"----------------------")
        return queryset


class CashflowRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Cashflow.objects.all()
    serializer_class = CashflowSerializer
