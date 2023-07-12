from rest_framework import serializers
from django.contrib.auth.hashers import make_password, check_password
from backend.user.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        new_user = User(
            email=validated_data["email"],
            password=make_password(validated_data["password"]),
        )
        new_user.save()
