from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from backend.user.api.viewsets import UserViewSet

router = DefaultRouter()
router.register(r"users", UserViewSet)


urlpatterns = [path("admin/", admin.site.urls), path("", include(router.urls))]
