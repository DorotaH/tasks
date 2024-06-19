from rest_framework import viewsets
from .serializers import TaskSerializer, UserSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .models import Task
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView


class TaskViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [BasicAuthentication]
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ["description", "name"]
    filterset_fields = ["id", "name", "status", "user"]


class GetUserView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer


class APIRootView(APIView):
    def get(self, request, format=None):
        return Response(
            {
                "create_user": request.build_absolute_uri(reverse("create_user")),
                "user": request.build_absolute_uri(reverse("user")),
                "tasks": request.build_absolute_uri(reverse("task-list")),
            }
        )
