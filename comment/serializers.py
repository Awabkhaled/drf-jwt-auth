from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    """A serializer for the data for the Comment model"""

    class Meta:
        model = Comment
        fields = ['id', 'text', 'user']
        read_only_fields = ['id', 'user']

    def create(self, validated_data):
        user = self.context.get('request').user
        validated_data['user'] = user
        comment = Comment.objects.create(**validated_data)
        return comment

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
