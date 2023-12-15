from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .models import *


class CategoryAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CatSerializer


class ProductAPIView(ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer


class OrderAPIView(APIView):
    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            order = serializer.save()
            return Response({'order_number': order.id}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListOrdersAPIView(APIView):
    def get(self, request):
        orders = Order.objects.all()
        order_ids = [order.id for order in orders]
        return Response({'orders_ids': order_ids}, status=status.HTTP_200_OK)


class OrderDetailAPIView(RetrieveAPIView):
        queryset = Order.objects.all()
        serializer_class = OrderDetailSerializer
        lookup_field = 'id'

        def retrieve(self, request, *args, **kwargs):
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            return Response(serializer.data, status=status.HTTP_200_OK)