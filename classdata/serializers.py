from rest_framework import serializers

from .models import User, UserClass, Class
from .validators import *


class UserRegistrationSerializer(serializers.ModelSerializer):
    """
    Serializer for User Registration
    """
    username = serializers.CharField(read_only=True)

    class Meta:
        model = User
        exclude = ("is_email_verified", "is_phone_verified", "is_staff", "is_active", "is_superuser", "password")

    def validate(self, attrs):
        if not (attrs.get("email") or attrs.get("phone")):
            raise ValidationError("email or phone number provide")
        attrs['username'] = attrs.get("email") or attrs.get("phone")
        return attrs

    def create(self, validated_data):
        """
        create entry in database
        :param validated_data:
        :return:
        """
        try:
            user = User.objects.create_user(**validated_data)
            return user
        except Exception as ex:
            raise ValidationError("User could not create"+repr(ex))



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
