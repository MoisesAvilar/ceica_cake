from rest_framework import generics, filters
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.db.models import Sum
from django.http import JsonResponse
from django.utils.dateparse import parse_datetime
from app.pagination import StandardResultsSetPagination

from sales.models import Sale
from sales.serializers import SaleSerializer, CheckoutSerializer
from sales.product_list import PRODUCT


class CheckoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = CheckoutSerializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=201)
        return Response(serializer.errors, status=400)


class SalesCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ["data_hour"]
    ordering = ["-data_hour"]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class SalesRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer

    def perform_update(self, serializer):
        serializer.save(user=self.get_object().user)


class ProductListView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        products = [{"value": key, "label": value} for key, value in PRODUCT]
        return JsonResponse(products, safe=False)


class SalesByProductView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        start_date = request.GET.get("start_date")
        end_date = request.GET.get("end_date")

        queryset = Sale.objects.all()

        if start_date and end_date:
            start_datetime = parse_datetime(start_date + "T00:00:00")
            end_datetime = parse_datetime(end_date + "T23:59:59")

            if start_datetime and end_datetime:
                queryset = queryset.filter(
                    data_hour__range=[start_datetime, end_datetime]
                )

        sales_data = (
            queryset.values("product")
            .annotate(total_sales=Sum("total"), quantity_sold=Sum("quantity"))
            .order_by("-total_sales")
        )
        return Response(sales_data)


class SalesByClientView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        start_date = request.GET.get("start_date")
        end_date = request.GET.get("end_date")

        queryset = Sale.objects.all()

        if start_date and end_date:
            start_datetime = parse_datetime(start_date + "T00:00:00")
            end_datetime = parse_datetime(end_date + "T23:59:59")

            if start_datetime and end_datetime:
                queryset = queryset.filter(
                    data_hour__range=[start_datetime, end_datetime]
                )

        sales_data = (
            queryset.values("customer__name")
            .annotate(total_sales=Sum("total"))
            .order_by("-total_sales")
        )
        return Response(sales_data)


class SalesByPeriodView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        start_date = request.GET.get("start_date")
        end_date = request.GET.get("end_date")

        if start_date and end_date:
            start_datetime = parse_datetime(start_date + "T00:00:00")
            end_datetime = parse_datetime(end_date + "T23:59:59")

            if not start_datetime or not end_datetime:
                return Response({"error": "Formato de data inválido"}, status=400)

            sales_data = (
                Sale.objects.filter(data_hour__range=[start_datetime, end_datetime])
                .values("product")
                .annotate(total_sales=Sum("total"), quantity_sold=Sum("quantity"))
            )

            return Response(sales_data)
        else:
            return Response(
                {"error": "start_date e end_date são obrigatórios"}, status=400
            )


class CustomerSalesHistoryView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = SaleSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        customer_id = self.kwargs["customer_id"]
        return Sale.objects.filter(customer__id=customer_id).order_by("-data_hour")
