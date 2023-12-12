from .models import *
from rest_framework import serializers


class CatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title', 'image')