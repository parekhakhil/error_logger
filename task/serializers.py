from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ['id','task','completed','created_at','updated_at','user']
        read_only_fields = ['created_at','updated_at']
        # write_only_fields = ['user_id']
