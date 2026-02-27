from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from customers.models import Customer
from customers.serializers import CustomerSerializer
from app.pagination import StandardResultsSetPagination
from rest_framework.filters import SearchFilter


class CustomerCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CustomerSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [SearchFilter]
    search_fields = ["name"]

    def get_queryset(self):
        queryset = Customer.objects.all().order_by("name")
        is_active = self.request.query_params.get("is_active")

        if is_active is not None:
            if is_active.lower() == "true":
                queryset = queryset.filter(is_active=True)
            elif is_active.lower() == "false":
                queryset = queryset.filter(is_active=False)

        return queryset


class CustomerRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def destroy(self, request, *args, **kwargs):
        from django.db.models import ProtectedError
        from rest_framework.response import Response
        from rest_framework import status

        try:
            return super().destroy(request, *args, **kwargs)
        except ProtectedError:
            return Response(
                {
                    "error": "Não é possível excluir este cliente porque existem vendas associadas a ele. Altere o status dele para 'Inativo' em vez de excluí-lo."
                },
                status=status.HTTP_400_BAD_REQUEST,
            )


class CustomerAllListView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Customer.objects.filter(is_active=True).order_by("name")
    serializer_class = CustomerSerializer
    pagination_class = None
