from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.db.models import Sum
from django.http import JsonResponse
from django.utils import timezone
from django.utils.dateparse import parse_datetime

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
        products = [{"value": key, "label": value} for key, value in PRODUCT]
        return JsonResponse(products, safe=False)


class SalesByProductView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        sales_data = (
            Sale.objects.values("product")
            .annotate(total_sales=Sum("total"), quantity_sold=Sum("quantity"))
            .order_by("-total_sales")
        )
        return Response(sales_data)


class SalesByClientView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        sales_data = (
            Sale.objects.values("customer__name")
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
            start_date = parse_datetime(start_date)
            end_date = parse_datetime(end_date)

            start_date = timezone.make_aware(
                start_date, timezone.get_current_timezone()
            )
            end_date = timezone.make_aware(end_date, timezone.get_current_timezone())

            sales_data = (
                Sale.objects.filter(data_hour__range=[start_date, end_date])
                .values("product")
                .annotate(total_sales=Sum("total"), quantity_sold=Sum("quantity"))
            )

            return Response(sales_data)
        else:
            return Response(
                {"error": "start_date and end_date are required"}, status=400
            )
