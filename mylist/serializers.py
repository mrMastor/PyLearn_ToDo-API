from rest_framework import serializers
from .models import ToList
from django.contrib.auth import get_user_model


class ItemSerializer(serializers.ModelSerializer):
    """Сериализатор по модели Item."""

    class Meta:
        model = ToList
        read_only_fields = ["id", "slug", "date_create", "date_complite"]
        fields = read_only_fields + ["status", "name"]
