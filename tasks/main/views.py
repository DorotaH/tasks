from rest_framework import viewsets
from .serializers import TaskSerializer, UserSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .models import Task
from rest_framework import generics


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ["description", "name"]
    filterset_fields = ["name", "status", "user"]


class GetUserView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer
