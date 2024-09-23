from django.urls import path
from sales.views import SalesCreateListView, SalesRetrieveUpdateDestroy, ProductListView


urlpatterns = [
    path("sales/", SalesCreateListView.as_view(), name="sales-create-list"),
    path(
        "sales/<int:pk>", SalesRetrieveUpdateDestroy.as_view(), name="sales-detail-view"
    ),
    path("products/", ProductListView.as_view(), name="product-list"),
]
