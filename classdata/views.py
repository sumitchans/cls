from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.status import *
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.exceptions import APIException

from .serializers import *


class UserRegisterView(APIView):
    """
    class to register User
    """
    permission_classes = (AllowAny, )

    def post(self, request):
        data = request.data
        serializer = UserRegistrationSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=HTTP_201_CREATED)
        return Response(data=serializers.errors, status=HTTP_400_BAD_REQUEST)


class UserLoginView(APIView):
    """
    class to user login
    """
    def post(self, request):
        data = request.data
        try:
            response = user_login(data, request)
            return Response(data=response.json(), status=response.status_code)
        except Exception as ex:
            raise APIException(str(ex))


class UserLogoutView(APIView):
    """
    class to user login
    """
    permission_classes = (IsAuthenticated, )

    def post(self, request):
        try:
            response = user_logout(request)
            return Response(data=response, status=response.status_code)
        except Exception as ex:
            raise APIException(str(ex))


class UserClassView(APIView):
    """
    class to user login
    """
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        try:
            response = get_user_class(request)
            return Response(data=response, status=200)
        except Exception as ex:
            raise APIException(str(ex))
