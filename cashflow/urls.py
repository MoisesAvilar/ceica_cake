from django.urls import path
from cashflow.views import CashflowCreateListView, CashflowRetrieveUpdateDestroyView


urlpatterns = [
    path("cashflow/", CashflowCreateListView.as_view(), name="cashflow-create-list"),
    path("cashflow/<int:pk>/", CashflowRetrieveUpdateDestroyView.as_view(), name="cashflow-detail-view"),
]
