from rest_framework import routers
from .api import ProjectViewSet, TodoListSerializers

router = routers.DefaultRouter()

router.register('api/projects', ProjectViewSet, 'projects')
# router.register('api/todolist', TodoListSerializers, 'todolist')


urlpatterns = router.urls