from .models import Order
from rest_framework import generics
from .serializers import OrderSerializer


class CreateOrder(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
