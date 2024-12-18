from rest_framework import serializers
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    """A serializer for the user model"""
    password = serializers.CharField(
        write_only=True,
        max_length=100
    )
    class Meta:
        model = get_user_model()
        fields = ['name', 'password']

    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)

        user = super().update(instance, validated_data)
        print(validated_data)
        if password:
            user.set_password(password)
            user.save()
        return user
