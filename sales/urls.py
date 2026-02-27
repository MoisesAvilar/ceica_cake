from django.urls import path
from sales.views import (
    SalesCreateListView,
    SalesRetrieveUpdateDestroy,
    ProductListView,
    SalesByProductView,
    SalesByClientView,
    SalesByPeriodView,
    CustomerSalesHistoryView,
    CheckoutView
)

urlpatterns = [
    path("checkout/", CheckoutView.as_view(), name="checkout"),
    path("sales/", SalesCreateListView.as_view(), name="sales-create-list"),
    path("sales/<int:pk>/", SalesRetrieveUpdateDestroy.as_view(), name="sales-detail-view"),
    path("products/", ProductListView.as_view(), name="product-list"),
    path("sales-by-product/", SalesByProductView.as_view(), name="sales-by-product"),
    path("sales-by-client/", SalesByClientView.as_view(), name="sales-by-client"),
    path("sales-by-period/", SalesByPeriodView.as_view(), name="sales-by-period"),
    path('customers/<int:customer_id>/sales/', CustomerSalesHistoryView.as_view(), name='customer-sales-history'),
]
