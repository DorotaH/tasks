from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

router = DefaultRouter()
router.register(r"tasks", views.TaskViewSet, basename="task")

urlpatterns = [
    path('create_user/', views.CreateUserView.as_view(), name='create_user'),
    path('user/', views.GetUserView.as_view(), name='user'),
    path('', views.APIRootView.as_view(), name='api-root'),
    path('', include(router.urls)),
]