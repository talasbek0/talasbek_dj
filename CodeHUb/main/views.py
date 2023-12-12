from rest_framework import generics
from .models import Category
from .serializers import *


class CategoryAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CatSerializer