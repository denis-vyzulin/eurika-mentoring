from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 
            'email',
            'username',
            'surname',
            'patronymic',
            'is_active',
            'is_staff',
        )
