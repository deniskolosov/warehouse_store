from django.urls import path
from .views import CreateOrder

urlpatterns = [
    path('orders/create/', CreateOrder.as_view())]

