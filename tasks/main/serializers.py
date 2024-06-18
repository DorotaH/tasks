from rest_framework.serializers import ModelSerializer
from .models import Task
from django.contrib.auth import get_user_model


class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = ["name", "description", "status", "user"]


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
