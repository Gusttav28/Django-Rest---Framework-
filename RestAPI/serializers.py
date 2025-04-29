from rest_framework import serializers
from .models import Project, TodoList


class ProjectSerializers(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
        read_only_fields = ('create_at',)
        

class TodoListSerializers(serializers.ModelSerializer):
    class Meta:
        model = TodoList
        fields = '__all__'
        read_only_fields = ('create_at',)