from django.urls import path
from .views import UpdateOrder

urlpatterns = [
    path('orders/update/<int:pk>', UpdateOrder.as_view()),
]
