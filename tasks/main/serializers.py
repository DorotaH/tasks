from rest_framework.serializers import ModelSerializer
from .models import Task
from django.contrib.auth import get_user_model
from simple_history.models import HistoricalRecords


class HistorySerializer(ModelSerializer):
    class Meta:
        model = Task.history.model
        fields = "__all__"


class TaskSerializer(ModelSerializer):
    history = HistorySerializer(source="history.all", many=True, read_only=True)

    class Meta:
        model = Task
        fields = ["id", "name", "description", "status", "user", "history"]
        read_only_fields = ["id", "history"]


class UserSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["username", "password", "email", "first_name", "last_name"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = get_user_model().objects.create_user(**validated_data)
        user.set_password(password)
        user.save()
        return user
