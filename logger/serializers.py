from .models import Error
from rest_framework import serializers


class ErrorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Error
        fields = "__all__"
        read_only_fields = [
            "created_at",
            "updated_at",
        ]
