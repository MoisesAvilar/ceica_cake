from django.urls import path
from customers.views import (
    CustomerCreateListView,
    CustomerRetrieveUpdateDestroyView,
    CustomerAllListView,
)


urlpatterns = [
    path("customers/", CustomerCreateListView.as_view(), name="customer-create-list"),
    path(
        "customers/<int:pk>/",
        CustomerRetrieveUpdateDestroyView.as_view(),
        name="customer-detail-view",
    ),
    path("customers/all/", CustomerAllListView.as_view(), name="customer-all-list"),
]
