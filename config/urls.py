from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from customers.views import CustomerViewSet
from support.views import ServiceRequestViewSet

router = DefaultRouter()
router.register(r'customers', CustomerViewSet)
router.register(r'service-requests', ServiceRequestViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]

