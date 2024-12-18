from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model
from .models import User


class UserSerializer(ModelSerializer):
    """A serializer for the user model"""
    class Meta:
        model = User
        fields = ['name', 'password']
    extra_kwargs = {
        'password': {
            'write_only': True,
            'max_length': 100
        }
    }

    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        user = super().update(instance, **validated_data)
        if password:
            user.set_password(password)
            user.save()
        return user
