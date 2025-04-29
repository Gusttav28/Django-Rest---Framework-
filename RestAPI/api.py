from .models import Project, TodoList
from rest_framework import viewsets, permissions
from .serializers import ProjectSerializers, TodoListSerializers



class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProjectSerializers
     
     
# class TodoListViewSet(viewsets.ModelViewSet):
#     queryset = TodoList.objects.all()
#     permission_classes = [permissions.AllowAny]
#     serializer_class = TodoListSerializers