from rest_framework import serializers

from .models import User, UserClass, Class
from .validators import *


class UserRegistrationSerializer(serializers.ModelSerializer):
    """
    Serializer for User Registration
    """
    class Meta:
        model = User
        exclude = ("is_email_verified", "is_phone_verified", "is_staff", "is_active", "is_superuser")

    def validate(self, attrs):
        if not (attrs.get("email") or attrs.get("phone")):
            raise ValidationError("email or phone number provide")
        return attrs


class ClassSerializer(serializers.ModelSerializer):
    """
    Class Serializer
    """
    class Meta:
        model = Class
        fields = '__all__'


class UserClassSerializer(serializers.ModelSerializer):
    """
    User Class serializer
    """
    class_id = ClassSerializer()

    class Meta:
        model = UserClass
        fields = '__all__'
