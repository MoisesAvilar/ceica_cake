from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/', include('authentication.urls')),
    path('api/v1/', include('cashflow.urls')),
    path('api/v1/', include('customers.urls')),
    path('api/v1/', include('sales.urls'))
]
